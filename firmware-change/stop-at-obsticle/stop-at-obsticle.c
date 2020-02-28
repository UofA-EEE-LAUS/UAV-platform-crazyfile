#include "deck.h"
#include "system.h"
#include "commander.h"
#include "crtp_commander_high_level.h"
#include <float.h>
#include "FreeRTOS.h"
#include "task.h"

#include "debug.h"

#include "log.h"

#define DEBUG_MODULE "PUSH"

typedef enum {
	idle, lowUnlock, unlocked, stopping
} State;

static State state = idle;

static const uint16_t unlockThHigh = 200;
static const uint16_t collisionTh = 170;

static uint16_t idUp = 0;
static uint16_t idDown = 0;
static uint16_t idLeft = 0;
static uint16_t idRight = 0;
static uint16_t idFront = 0;
static uint16_t idBack = 0;

static uint16_t up = 0;
static uint16_t down = 0;
static uint16_t front = 0;
static uint16_t back = 0;
static uint16_t left = 0;
static uint16_t right = 0;


#define MAX(a,b) ((a>b)?a:b)
#define MIN(a,b) ((a<b)?a:b)

static void sequenceTask() {
	static setpoint_t setpoint;

	systemWaitStart();

	vTaskDelay(M2T(3000));

	idUp = logGetVarId("range", "up");
	idDown = logGetVarId("range", "zrange");
	idLeft = logGetVarId("range", "left");
	idRight = logGetVarId("range", "right");
	idFront = logGetVarId("range", "front");
	idBack = logGetVarId("range", "back");

	DEBUG_PRINT("Waiting for activation ...\n");

	while (1) {
		vTaskDelay(M2T(100));
		//DEBUG_PRINT(".");
		down = logGetUint(idDown); //check height for unlocking coll avoid

		if (state == unlocked) {
			up = logGetUint(idUp);
			left = logGetUint(idLeft);
			right = logGetUint(idRight);
			front = logGetUint(idFront);
			back = logGetUint(idBack);

			if (front<collisionTh && front>0 || left<collisionTh && left>0 || right<collisionTh && right>0 || back<collisionTh && back>0) {
				//DEBUG_PRINT("coll. detected\n");
				float timeToStop = 0.65;
				crtpCommanderHighLevelGoTo(0, 0, 0, 0.0, timeToStop, true, 0);
				vTaskDelay(M2T(1500)); //chance to move in opposite direction
			}


		} else {


			if (down > unlockThHigh && state == idle) {
				DEBUG_PRINT("coll. avoid unlocked!\n");
				state = unlocked;
			}


		}
	}
}

static void sequenceInit() {
	xTaskCreate(sequenceTask, "sequence", 2*configMINIMAL_STACK_SIZE, NULL,
	/*priority*/3, NULL);
}

static bool sequenceTest() {
	return true;
}

const DeckDriver sequence_deck = { .vid = 0, .pid = 0, .name = "bcPush",

.usedGpio = 0,  // FIXME: set the used pins

		.init = sequenceInit, .test = sequenceTest, };

DECK_DRIVER(sequence_deck);