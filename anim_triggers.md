# Cozmo Animation Triggers

Full list of `cozmo.anim.Triggers` names, extracted from the locally installed SDK
(`cozmo` 1.4.12 / `cozmoclad` 3.6.6). Generated because the official docs site
(`cozmosdk.anki.bot`) is offline. **576 triggers total**, grouped by theme and sorted alphabetically within each group.

Usage:

```python
robot.play_anim_trigger(cozmo.anim.Triggers.<Name>).wait_for_completed()
```

To regenerate this list against whatever SDK version you have installed:

```python
import cozmo.anim as anim
names = sorted(t.name for t in anim.Triggers.trigger_list)
```

## Categories

| Category | Count |
|---|---|
| [Code Lab (Scratch Blocks)](#code-lab-scratch-blocks) | 67 |
| [Miscellaneous](#miscellaneous) | 50 |
| [Repair Minigame](#repair-minigame) | 32 |
| [Feeding Minigame](#feeding-minigame) | 30 |
| [Memory Match Game](#memory-match-game) | 24 |
| [Onboarding (First Setup)](#onboarding-first-setup) | 22 |
| [Needs (Severe)](#needs-severe) | 21 |
| [Reactions (General)](#reactions-general) | 20 |
| [Speed Tap Game](#speed-tap-game) | 20 |
| [Workout Minigame](#workout-minigame) | 19 |
| [Cube Pounce Game](#cube-pounce-game) | 15 |
| [Hiking / Exploring](#hiking-exploring) | 14 |
| [Driving Moods](#driving-moods) | 12 |
| [Drone Mode](#drone-mode) | 12 |
| [Game Request: Keep Away](#game-request-keep-away) | 12 |
| [Game Request: Memory Match](#game-request-memory-match) | 12 |
| [Game Request: Speed Tap](#game-request-speed-tap) | 12 |
| [Spark / Upgrade](#spark-upgrade) | 12 |
| [Cozmo Says](#cozmo-says) | 11 |
| [Guard Dog Minigame](#guard-dog-minigame) | 11 |
| [Voice Command](#voice-command) | 11 |
| [Build Pyramid](#build-pyramid) | 10 |
| [Meet Cozmo (Face Enrollment)](#meet-cozmo-face-enrollment) | 10 |
| [Peek-a-Boo](#peek-a-boo) | 10 |
| [Bouncer Minigame](#bouncer-minigame) | 9 |
| [Pounce Game](#pounce-game) | 9 |
| [Hiccup](#hiccup) | 7 |
| [Laser Pointer Game](#laser-pointer-game) | 7 |
| [Roll Block](#roll-block) | 7 |
| [Dizzy / Off-Balance](#dizzy-off-balance) | 6 |
| [Knock Over](#knock-over) | 6 |
| [Pet Detection](#pet-detection) | 6 |
| [Sound-Only (No Motion)](#sound-only-no-motion) | 6 |
| [Fist Bump](#fist-bump) | 5 |
| [Pop-a-Wheelie](#pop-a-wheelie) | 5 |
| [Singing](#singing) | 5 |
| [Boredom](#boredom) | 4 |
| [Game Setup](#game-setup) | 4 |
| [Sleep](#sleep) | 4 |
| [Come Here](#come-here) | 3 |
| [Connect / Wake Up](#connect-wake-up) | 3 |
| [Needs (Mild)](#needs-mild) | 3 |
| [Cube Reactions](#cube-reactions) | 2 |
| [Face Search](#face-search) | 2 |
| [Game Request (General)](#game-request-general) | 2 |
| [Pickup Helper](#pickup-helper) | 2 |
| **Total** | **576** |

## Code Lab (Scratch Blocks)

- `CodeLab123Go`
- `CodeLabAmazed`
- `CodeLabBlink`
- `CodeLabBored`
- `CodeLabCat`
- `CodeLabCelebrate`
- `CodeLabChatty`
- `CodeLabChicken`
- `CodeLabConducting`
- `CodeLabCow`
- `CodeLabCurious`
- `CodeLabDancingMambo`
- `CodeLabDejected`
- `CodeLabDizzy`
- `CodeLabDizzyEnd`
- `CodeLabDog`
- `CodeLabDuck`
- `CodeLabElephant`
- `CodeLabEnergyEat`
- `CodeLabEnter`
- `CodeLabExcited`
- `CodeLabExit`
- `CodeLabFireTruck`
- `CodeLabFrog`
- `CodeLabFrustrated`
- `CodeLabGetInPos`
- `CodeLabGhoul`
- `CodeLabHappy`
- `CodeLabHeadsUp`
- `CodeLabHelium`
- `CodeLabHiccup`
- `CodeLabIDK`
- `CodeLabIdle`
- `CodeLabLose`
- `CodeLabNo`
- `CodeLabPartyTime`
- `CodeLabRattleSnake`
- `CodeLabReactHappy`
- `CodeLabRooster`
- `CodeLabScaredCozmo`
- `CodeLabScaryCozmo`
- `CodeLabSheep`
- `CodeLabSleep`
- `CodeLabSneeze`
- `CodeLabSquint1`
- `CodeLabSquint2`
- `CodeLabStaring`
- `CodeLabSurprise`
- `CodeLabTakaTaka`
- `CodeLabTapCube`
- `CodeLabThinking`
- `CodeLabTiger`
- `CodeLabTwitch`
- `CodeLabUnhappy`
- `CodeLabVampire`
- `CodeLabVictory`
- `CodeLabWhee1`
- `CodeLabWhee2`
- `CodeLabWhee3`
- `CodeLabWhee4`
- `CodeLabWhew`
- `CodeLabWhoa`
- `CodeLabWin`
- `CodeLabWondering`
- `CodeLabYes`
- `CodeLabYuck`
- `CodeLabZombie`

## Miscellaneous

- `AcknowledgeFaceInitPause`
- `AcknowledgeFaceNamed`
- `AcknowledgeFaceUnnamed`
- `AcknowledgeObject`
- `AskToBeRightedLeft`
- `AskToBeRightedRight`
- `AudioTestAnim`
- `BlockReact`
- `CantHandleTallStack`
- `Count`
- `DanceMambo`
- `EarnedSparks`
- `FacePlantRoll`
- `FacePlantRollArmUp`
- `FailedToRightFromFace`
- `FlipDownFromBack`
- `FrustratedByFailure`
- `FrustratedByFailureMajor`
- `IdleOnCharger`
- `InteractWithFaceTrackingIdle`
- `InteractWithFacesInitialNamed`
- `InteractWithFacesInitialUnnamed`
- `MajorFail`
- `MajorWin`
- `NamedFaceInitialGreeting`
- `NeutralFace`
- `OnLearnedPlayerName`
- `OnSawNewNamedFace`
- `OnSawNewUnnamedFace`
- `OnSawOldNamedFace`
- `OnSawOldUnnamedFace`
- `OnWaitForCubesMinigameSetup`
- `OnWiggle`
- `PatternGuessNewIdea`
- `PatternGuessThinking`
- `PlacedOnCharger`
- `ProceduralLive`
- `PutDownBlockKeepAlive`
- `PutDownBlockPutDown`
- `SdkTextToSpeech`
- `Shiver`
- `Shocked`
- `Sleeping`
- `StackBlocksSuccess`
- `StartSleeping`
- `SuccessfulWheelie`
- `Surprise`
- `TurtleRoll`
- `UnitTestAnim`
- `WaitOnSideLoop`

## Repair Minigame

- `RepairFailMild`
- `RepairFailSevere`
- `RepairFixMildGetIn`
- `RepairFixMildGetOut`
- `RepairFixMildGetReady`
- `RepairFixMildHeadDown`
- `RepairFixMildHeadUp`
- `RepairFixMildIdle`
- `RepairFixMildLiftDown`
- `RepairFixMildLiftUp`
- `RepairFixMildLowerLift`
- `RepairFixMildRaiseLift`
- `RepairFixMildRoundReact`
- `RepairFixMildWheelsBack`
- `RepairFixMildWheelsForward`
- `RepairFixSevereGetIn`
- `RepairFixSevereGetOut`
- `RepairFixSevereGetReady`
- `RepairFixSevereHeadDown`
- `RepairFixSevereHeadUp`
- `RepairFixSevereIdle`
- `RepairFixSevereLiftDown`
- `RepairFixSevereLiftUp`
- `RepairFixSevereLowerLift`
- `RepairFixSevereRaiseLift`
- `RepairFixSevereRoundReact`
- `RepairFixSevereWheelsBack`
- `RepairFixSevereWheelsForward`
- `RepairIdleFullyRepaired`
- `RepairPartRepaired_Head_Mild`
- `RepairPartRepaired_Lift_Mild`
- `RepairPartRepaired_Tread_Mild`

## Feeding Minigame

- `FeedingAteFullEnough_Normal`
- `FeedingAteFullEnough_Severe`
- `FeedingAteNotFullEnough_Normal`
- `FeedingAteNotFullEnough_Severe`
- `FeedingDrivingGetIn_Severe`
- `FeedingDrivingGetOut_Severe`
- `FeedingDrivingLoop_Severe`
- `FeedingIdleSearchForFaces_Normal`
- `FeedingIdleSearchForFaces_Severe`
- `FeedingIdleSearch_Normal`
- `FeedingIdleSearch_Severe`
- `FeedingIdleWaitForFullCube_Normal`
- `FeedingIdleWaitForFullCube_Severe`
- `FeedingIdleWaitForShakeNoHead_Severe`
- `FeedingIdleWaitForShake_Normal`
- `FeedingIdleWaitForShake_Severe`
- `FeedingInterrupted`
- `FeedingInterrupted_Severe`
- `FeedingPlaceLiftOnCube_Normal`
- `FeedingPlaceLiftOnCube_Severe`
- `FeedingReactToFullCube_Normal`
- `FeedingReactToFullCube_Severe`
- `FeedingReactToSeeCube_Normal`
- `FeedingReactToSeeCube_Severe`
- `FeedingReactToShake_Normal`
- `FeedingReactToShake_Severe`
- `FeedingSearchFailure`
- `FeedingSearchFailure_Severe`
- `FeedingSearchRequest`
- `FeedingSearchRequest_Severe`

## Memory Match Game

- `MemoryMatchCozmoFollowTapsSoundOnly`
- `MemoryMatchCozmoGetOut`
- `MemoryMatchCozmoLoseHand`
- `MemoryMatchCozmoWinGame`
- `MemoryMatchCozmoWinHand`
- `MemoryMatchPlayerLoseHand`
- `MemoryMatchPlayerLoseHandSolo`
- `MemoryMatchPlayerWinGame`
- `MemoryMatchPlayerWinHand`
- `MemoryMatchPlayerWinHandLong`
- `MemoryMatchPlayerWinHandSolo`
- `MemoryMatchPointCenter`
- `MemoryMatchPointCenterFast`
- `MemoryMatchPointLeftBig`
- `MemoryMatchPointLeftBigFast`
- `MemoryMatchPointLeftSmall`
- `MemoryMatchPointLeftSmallFast`
- `MemoryMatchPointRightBig`
- `MemoryMatchPointRightBigFast`
- `MemoryMatchPointRightSmall`
- `MemoryMatchPointRightSmallFast`
- `MemoryMatchReactToPattern`
- `MemoryMatchReactToPatternSolo`
- `MemoryMatchSoloGameOver`

## Onboarding (First Setup)

- `OnboardingBirth`
- `OnboardingCubeDockFail`
- `OnboardingDiscoverCube`
- `OnboardingDriveEnd`
- `OnboardingDriveLoop`
- `OnboardingDriveStart`
- `OnboardingEyesOn`
- `OnboardingGetOut`
- `OnboardingHelloPlayer`
- `OnboardingHelloWorld`
- `OnboardingIdle`
- `OnboardingIdleEnergy`
- `OnboardingIdlePlay`
- `OnboardingIdleRepair`
- `OnboardingInteractWithCube`
- `OnboardingPreBirth`
- `OnboardingReactToCube`
- `OnboardingReactToCubePutDown`
- `OnboardingReactToFace`
- `OnboardingSoundOnlyLiftEffortPickup`
- `OnboardingSoundOnlyLiftEffortPlaceLow`
- `OnboardingWakeUpDriveOffCharger`

## Needs (Severe)

- `NeedsSevereLowEnergyCliffReact`
- `NeedsSevereLowEnergyDrivingEnd`
- `NeedsSevereLowEnergyDrivingLoop`
- `NeedsSevereLowEnergyDrivingStart`
- `NeedsSevereLowEnergyForceGetOut`
- `NeedsSevereLowEnergyGetIn`
- `NeedsSevereLowEnergyIdle`
- `NeedsSevereLowEnergyRequest`
- `NeedsSevereLowEnergySlopeReact`
- `NeedsSevereLowPlayForceGetOut`
- `NeedsSevereLowPlayGetIn`
- `NeedsSevereLowPlayRequest`
- `NeedsSevereLowRepairCliffReact`
- `NeedsSevereLowRepairDrivingEnd`
- `NeedsSevereLowRepairDrivingLoop`
- `NeedsSevereLowRepairDrivingStart`
- `NeedsSevereLowRepairForceGetOut`
- `NeedsSevereLowRepairGetIn`
- `NeedsSevereLowRepairIdle`
- `NeedsSevereLowRepairRequest`
- `NeedsSevereLowRepairSlopeReact`

## Reactions (General)

- `ReactToBlockPickupSuccess`
- `ReactToBlockRetryPickup`
- `ReactToCliff`
- `ReactToCliffDetectorStop`
- `ReactToFalling`
- `ReactToImpact`
- `ReactToMotorCalibration`
- `ReactToNewBlockAsk`
- `ReactToNewBlockBig`
- `ReactToNewBlockSmall`
- `ReactToObstacle`
- `ReactToOnLeftSide`
- `ReactToOnRightSide`
- `ReactToPerchedOnBlock`
- `ReactToPickup`
- `ReactToPokeReaction`
- `ReactToPokeStartled`
- `ReactToUnexpectedMovement`
- `ReactToUnexpectedMovement_Severe_Energy`
- `ReactToUnexpectedMovement_Severe_Repair`

## Speed Tap Game

- `DemoSpeedTapCozmoLose`
- `DemoSpeedTapCozmoWin`
- `OnSpeedtapCozmoConfirm`
- `OnSpeedtapFakeout`
- `OnSpeedtapGameCozmoWinHighIntensity`
- `OnSpeedtapGameCozmoWinLowIntensity`
- `OnSpeedtapGamePlayerWinHighIntensity`
- `OnSpeedtapGamePlayerWinLowIntensity`
- `OnSpeedtapGetOut`
- `OnSpeedtapHandCozmoWin`
- `OnSpeedtapHandPlayerWin`
- `OnSpeedtapIdle`
- `OnSpeedtapRoundCozmoWinHighIntensity`
- `OnSpeedtapRoundCozmoWinLowIntensity`
- `OnSpeedtapRoundPlayerWinHighIntensity`
- `OnSpeedtapRoundPlayerWinLowIntensity`
- `OnSpeedtapTap`
- `SpeedTapDrivingEnd`
- `SpeedTapDrivingLoop`
- `SpeedTapDrivingStart`

## Workout Minigame

- `WorkoutPostLift_highEnergy`
- `WorkoutPostLift_lowEnergy`
- `WorkoutPostLift_mediumEnergy`
- `WorkoutPreLift_highEnergy`
- `WorkoutPreLift_lowEnergy`
- `WorkoutPreLift_mediumEnergy`
- `WorkoutPutDown_highEnergy`
- `WorkoutPutDown_lowEnergy`
- `WorkoutPutDown_lowEnergy_simple`
- `WorkoutPutDown_mediumEnergy`
- `WorkoutStrongLift_highEnergy`
- `WorkoutStrongLift_lowEnergy`
- `WorkoutStrongLift_mediumEnergy`
- `WorkoutTransition_highEnergy`
- `WorkoutTransition_lowEnergy`
- `WorkoutTransition_mediumEnergy`
- `WorkoutWeakLift_highEnergy`
- `WorkoutWeakLift_lowEnergy`
- `WorkoutWeakLift_mediumEnergy`

## Cube Pounce Game

- `CubePounceFake`
- `CubePounceGetIn`
- `CubePounceGetOut`
- `CubePounceGetReady`
- `CubePounceGetUnready`
- `CubePounceIdleLiftDown`
- `CubePounceIdleLiftUp`
- `CubePounceLoseHand`
- `CubePounceLoseRound`
- `CubePounceLoseSession`
- `CubePouncePounceClose`
- `CubePouncePounceNormal`
- `CubePounceWinHand`
- `CubePounceWinRound`
- `CubePounceWinSession`

## Hiking / Exploring

- `HikingDrivingEnd`
- `HikingDrivingLoop`
- `HikingDrivingStart`
- `HikingInterestingEdgeThought`
- `HikingIntro`
- `HikingLookAround`
- `HikingObserve`
- `HikingReactToEdge`
- `HikingReactToNewArea`
- `HikingReactToPossibleMarker`
- `HikingSquintEnd`
- `HikingSquintLoop`
- `HikingSquintStart`
- `HikingWakeUpOffCharger`

## Driving Moods

- `DriveEndAngry`
- `DriveEndDefault`
- `DriveEndHappy`
- `DriveEndLaunch`
- `DriveLoopAngry`
- `DriveLoopDefault`
- `DriveLoopHappy`
- `DriveLoopLaunch`
- `DriveStartAngry`
- `DriveStartDefault`
- `DriveStartHappy`
- `DriveStartLaunch`

## Drone Mode

- `DroneModeBackwardDrivingEnd`
- `DroneModeBackwardDrivingLoop`
- `DroneModeBackwardDrivingStart`
- `DroneModeCliffEvent`
- `DroneModeForwardDrivingEnd`
- `DroneModeForwardDrivingLoop`
- `DroneModeForwardDrivingStart`
- `DroneModeGetIn`
- `DroneModeGetOut`
- `DroneModeIdle`
- `DroneModeKeepAlive`
- `DroneModeTurboDrivingStart`

## Game Request: Keep Away

- `RequestGameKeepAwayAccept0`
- `RequestGameKeepAwayAccept1`
- `RequestGameKeepAwayDeny0`
- `RequestGameKeepAwayDeny1`
- `RequestGameKeepAwayIdle0`
- `RequestGameKeepAwayIdle1`
- `RequestGameKeepAwayInitial0`
- `RequestGameKeepAwayInitial1`
- `RequestGameKeepAwayPreDrive0`
- `RequestGameKeepAwayPreDrive1`
- `RequestGameKeepAwayRequest0`
- `RequestGameKeepAwayRequest1`

## Game Request: Memory Match

- `RequestGameMemoryMatchAccept0`
- `RequestGameMemoryMatchAccept1`
- `RequestGameMemoryMatchDeny0`
- `RequestGameMemoryMatchDeny1`
- `RequestGameMemoryMatchIdle0`
- `RequestGameMemoryMatchIdle1`
- `RequestGameMemoryMatchInitial0`
- `RequestGameMemoryMatchInitial1`
- `RequestGameMemoryMatchPreDrive0`
- `RequestGameMemoryMatchPreDrive1`
- `RequestGameMemoryMatchRequest0`
- `RequestGameMemoryMatchRequest1`

## Game Request: Speed Tap

- `RequestGameSpeedTapAccept0`
- `RequestGameSpeedTapAccept1`
- `RequestGameSpeedTapDeny0`
- `RequestGameSpeedTapDeny1`
- `RequestGameSpeedTapIdle0`
- `RequestGameSpeedTapIdle1`
- `RequestGameSpeedTapInitial0`
- `RequestGameSpeedTapInitial1`
- `RequestGameSpeedTapPreDrive0`
- `RequestGameSpeedTapPreDrive1`
- `RequestGameSpeedTapRequest0`
- `RequestGameSpeedTapRequest1`

## Spark / Upgrade

- `SoftSparkUpgradeLift`
- `SoftSparkUpgradeTracks`
- `SparkDrivingLoop`
- `SparkDrivingStart`
- `SparkDrivingStop`
- `SparkFailure`
- `SparkGetIn`
- `SparkGetOut`
- `SparkIdle`
- `SparkPickupFinalCubeReaction`
- `SparkPickupInitialCubeReaction`
- `SparkSuccess`

## Cozmo Says

- `CozmoSaysBadWord`
- `CozmoSaysGetIn`
- `CozmoSaysGetOut`
- `CozmoSaysIdle`
- `CozmoSaysSpeakGetInLong`
- `CozmoSaysSpeakGetInMedium`
- `CozmoSaysSpeakGetInShort`
- `CozmoSaysSpeakGetOutLong`
- `CozmoSaysSpeakGetOutMedium`
- `CozmoSaysSpeakGetOutShort`
- `CozmoSaysSpeakLoop`

## Guard Dog Minigame

- `GuardDogBusted`
- `GuardDogCubeDisconnect`
- `GuardDogFakeout`
- `GuardDogInterruption`
- `GuardDogPlayerSuccess`
- `GuardDogPulse`
- `GuardDogSettle`
- `GuardDogSleepLoop`
- `GuardDogTimeout`
- `GuardDogTimeoutCubesTouched`
- `GuardDogTimeoutCubesUntouched`

## Voice Command

- `VC_Alrighty`
- `VC_HowAreYouDoing_AllGood`
- `VC_Listening`
- `VC_LookDownForLaser`
- `VC_LookDownNoLaser`
- `VC_NoFollowupCommand_NoFace`
- `VC_NoFollowupCommand_WithFace`
- `VC_Refuse_energy`
- `VC_Refuse_repair`
- `VC_Refuse_sparks`
- `VC_StartledWakeup`

## Build Pyramid

- `BuildPyramidFirstBlockOnSide`
- `BuildPyramidFirstBlockUpright`
- `BuildPyramidLookForFace`
- `BuildPyramidReactToBase`
- `BuildPyramidSecondBlockOnSide`
- `BuildPyramidSecondBlockUpright`
- `BuildPyramidSuccess`
- `BuildPyramidThankUser`
- `BuildPyramidThirdBlockOnSide`
- `BuildPyramidThirdBlockUpright`

## Meet Cozmo (Face Enrollment)

- `MeetCozmoFirstEnrollmentCelebration`
- `MeetCozmoFirstEnrollmentRepeatName`
- `MeetCozmoFirstEnrollmentSayName`
- `MeetCozmoGetIn`
- `MeetCozmoLookFaceGetIn`
- `MeetCozmoLookFaceGetOut`
- `MeetCozmoLookFaceInterrupt`
- `MeetCozmoReEnrollmentSayName`
- `MeetCozmoRenameFaceSayName`
- `MeetCozmoScanningIdle`

## Peek-a-Boo

- `PeekABooGetIn`
- `PeekABooGetOutHappy`
- `PeekABooGetOutSad`
- `PeekABooHighIntensity`
- `PeekABooIdle`
- `PeekABooLowIntensity`
- `PeekABooMedIntensity`
- `PeekABooNoUserInteraction`
- `PeekABooShort`
- `PeekABooSurprised`

## Bouncer Minigame

- `BouncerGetIn`
- `BouncerGetOut`
- `BouncerIdeaToPlay`
- `BouncerIntoScore1`
- `BouncerIntoScore2`
- `BouncerIntoScore3`
- `BouncerRequestToPlay`
- `BouncerTimeout`
- `BouncerWait`

## Pounce Game

- `PounceDriveEnd`
- `PounceDriveLoop`
- `PounceDriveStart`
- `PounceFace`
- `PounceFail`
- `PounceGetOut`
- `PounceInitial`
- `PouncePounce`
- `PounceSuccess`

## Hiccup

- `Hiccup`
- `HiccupGetIn`
- `HiccupPlayerCure`
- `HiccupRobotOnBack`
- `HiccupRobotOnFace`
- `HiccupRobotPickedUp`
- `HiccupSelfCure`

## Laser Pointer Game

- `LaserAcknowledge`
- `LaserDriveEnd`
- `LaserDriveLoop`
- `LaserDriveStart`
- `LaserFace`
- `LaserGetOut`
- `LaserPounce`

## Roll Block

- `RollBlockInitial`
- `RollBlockPreActionNamedFace`
- `RollBlockPreActionUnnamedFace`
- `RollBlockPutDown`
- `RollBlockRealign`
- `RollBlockRetry`
- `RollBlockSuccess`

## Dizzy / Off-Balance

- `DizzyReactionHard`
- `DizzyReactionMedium`
- `DizzyReactionSoft`
- `DizzyShakeLoop`
- `DizzyShakeStop`
- `DizzyStillPickedUp`

## Knock Over

- `KnockOverEyes`
- `KnockOverFailure`
- `KnockOverGrabAttempt`
- `KnockOverPreActionNamedFace`
- `KnockOverPreActionUnnamedFace`
- `KnockOverSuccess`

## Pet Detection

- `PetDetectionCat`
- `PetDetectionDog`
- `PetDetectionShort`
- `PetDetectionShort_Cat`
- `PetDetectionShort_Dog`
- `PetDetectionSneeze`

## Sound-Only (No Motion)

- `SoundOnlyLiftEffortPickup`
- `SoundOnlyLiftEffortPlaceHigh`
- `SoundOnlyLiftEffortPlaceLow`
- `SoundOnlyLiftEffortPlaceRoll`
- `SoundOnlyRamIntoBlock`
- `SoundOnlyTurnSmall`

## Fist Bump

- `FistBumpIdle`
- `FistBumpLeftHanging`
- `FistBumpRequestOnce`
- `FistBumpRequestRetry`
- `FistBumpSuccess`

## Pop-a-Wheelie

- `PopAWheelieInitial`
- `PopAWheeliePreActionNamedFace`
- `PopAWheeliePreActionUnnamedFace`
- `PopAWheelieRealign`
- `PopAWheelieRetry`

## Singing

- `Singing_100bpm`
- `Singing_120bpm`
- `Singing_80bpm`
- `Singing_GetIn`
- `Singing_GetOut`

## Boredom

- `NothingToDoBoredEvent`
- `NothingToDoBoredIdle`
- `NothingToDoBoredIntro`
- `NothingToDoBoredOutro`

## Game Setup

- `GameSetupGetIn`
- `GameSetupGetOut`
- `GameSetupIdle`
- `GameSetupReaction`

## Sleep

- `GoToSleepGetIn`
- `GoToSleepGetOut`
- `GoToSleepOff`
- `GoToSleepSleeping`

## Come Here

- `ComeHere_AlreadyHere`
- `ComeHere_SearchForFace`
- `ComeHere_SearchForFace_FoundFace`

## Connect / Wake Up

- `ConnectWakeUp`
- `ConnectWakeUp_SevereEnergy`
- `ConnectWakeUp_SevereRepair`

## Needs (Mild)

- `NeedsMildLowEnergyRequest`
- `NeedsMildLowPlayRequest`
- `NeedsMildLowRepairRequest`

## Cube Reactions

- `CubeMovedSense`
- `CubeMovedUpset`

## Face Search

- `LookInPlaceForFacesBodyPause`
- `LookInPlaceForFacesHeadMovePause`

## Game Request (General)

- `RequestGameInterrupt`
- `RequestGamePickupFail`

## Pickup Helper

- `PickupHelperPreActionNamedFace`
- `PickupHelperPreActionUnnamedFace`
