// journey-to-ascension_inject.js

// Variable outside tick() to persist state across interval loops
var pendingZoneRestore;

var journeyResetCount;
journeyResetCount = (journeyResetCount !== undefined)
    ? journeyResetCount
    : 0;

function setTabStatus(status) {
    'use strict';
    // Strip previous tag if present, then prepend new status
    var cleanTitle = document.title.replace(/^\[.*?\]\s*/, '');
    document.title = '[' + status + '] ' + cleanTitle;
}

function logBot(message, isAlert) {
    'use strict';
    if (message === '') {
        return;
    }
    var bgColor = isAlert
        ? '#ef4444'
        : '#22c55e';  // Red for alert/reset, Green for normal
    var textColor = isAlert
        ? '#ffffff'
        : '#000000'; // White text on red, Black text on green
    var badgeStyle = 'background: ' + bgColor + '; color: ' + textColor + '; font-weight: bold; padding: 2px 6px; border-radius: 3px;';

    console.log('%c BOT %c ' + message, badgeStyle, 'color: inherit;');
}

function updateHUD(statusText, isGameOver) {
    'use strict';
    var hud = document.getElementById('journey-hud');

    // Inject HUD element if it doesn't exist yet
    if (!hud) {
        hud = document.createElement('div');
        hud.id = 'journey-hud';
        hud.style.cssText = '' +
                'position: fixed; top: 10px; right: 10px; z-index: 999999; ' +
                'background: rgba(15, 23, 42, 0.9); color: #f8fafc; padding: 8px 14px; ' +
                'border-radius: 8px; font-family: monospace; font-size: 12px; ' +
                'border: 1px solid #334155; box-shadow: 0 4px 12px rgba(0,0,0,0.4); ' +
                'pointer-events: none;';
        document.body.appendChild(hud);
    }

    var statusColor = isGameOver
        ? '#ef4444'
        : '#22c55e'; // Red on Game Over, Green when Running

    hud.innerHTML =
            '<b>[Journey Bot]</b> ' +
            'Status: <span style="color:' + statusColor + '; font-weight:bold;">' + statusText + '</span> | ' +
            'Resets: <span style="color:#38bdf8;">' + journeyResetCount + '</span>';
}

function notifyBot(statusText, message, isAlert) {
    'use strict';
    updateHUD(statusText, isAlert);
    setTabStatus(statusText);
    logBot(message, isAlert);
}

// Helper function to find the reset buttons inside the overlay
function getResetButtons() {
    'use strict';
    const overlay = document.getElementById('game-over-overlay');
    if (!overlay) {
        return {
            withAuto: null,
            withoutAuto: null
        };
    }

    // Get all buttons inside overlay and find them by text content
    const buttons = Array.from(overlay.querySelectorAll('button'));

    return {
        withAuto: buttons.find((btn) => btn.innerText.includes('With Auto Use Items')) || null,
        withoutAuto: buttons.find((btn) => btn.innerText.includes('Without Auto Use Items')) || null
    };
}

function getControls() {
    'use strict';
    const controlsList = document.getElementById('controls-list');
    if (!controlsList) {
        return null;
    }

    // Grab buttons by row hierarchy
    const rowButtons = controlsList.querySelectorAll('.controls-row button');
    const autoButtons = controlsList.querySelectorAll('.automation-controls > button');

    return {
        repeatTasks: rowButtons[0] || null,
        autoUseItems: rowButtons[1] || null,
        toZone: autoButtons[0] || null,
        currentZone: autoButtons[1] || null
    };
}

function getControlsState() {
    'use strict';
    const controls = getControls();
    if (!controls) {
        return null;
    }

    // Helper to check if an element has the 'on' class
    const isOn = (el) => el
        ? el.classList.contains('on')
        : false;

    // Helper to get clean, whitespace-trimmed text
    const getText = (el) => el
        ? el.innerText.trim()
        : '';

    const repeatText = getText(controls.repeatTasks);
    const autoItemsText = getText(controls.autoUseItems);

    return {
        // Boolean flags for easy conditionally checked logic
        isRepeatingTasks: repeatText === 'Repeat Tasks',
        isAutoUsingItems: autoItemsText === 'Auto Use Items',

        // Mode flags based on class="on"
        toZoneActive: isOn(controls.toZone),
        currentZoneActive: isOn(controls.currentZone),

        // Raw text labels if you need exact string checks
        repeatText,
        autoItemsText,

        // Direct DOM references in case we need to trigger .click() on them later
        elements: controls
    };
}

function journey_tick() {
    'use strict';
    const overlay = document.getElementById('game-over-overlay');
    const isOverlayVisible = overlay && !overlay.classList.contains('hidden');

    // ------------------------------------------------------------------
    // PHASE 1: GAME OVER OVERLAY IS VISIBLE
    // ------------------------------------------------------------------
    if (isOverlayVisible) {
        const state = getControlsState();
        if (!state) {
            console.error('No state!');
            return;
        }

        // 1. Record which zone button was active so we can restore it post-reset
        if (state.toZoneActive) {
            pendingZoneRestore = 'toZone';
        } else if (state.currentZoneActive) {
            pendingZoneRestore = 'currentZone';
        } else {
            pendingZoneRestore = null;
        }

        // 2. Grab the reset buttons
        const resetBtns = getResetButtons();

        // 3. Click the matching reset button based on item auto-use setting
        if (state.isAutoUsingItems && resetBtns.withAuto) {
            notifyBot('RESETTING', 'Game Over detected -> Clicking "Reset, With Auto Use Items"', true);
            resetBtns.withAuto.click();
        } else if (!state.isAutoUsingItems && resetBtns.withoutAuto) {
            notifyBot('RESETTING', 'Game Over detected -> Clicking "Reset, Without Auto Use Items"', true);
            resetBtns.withoutAuto.click();
        } else {
            console.warn('Could not locate appropriate reset button on overlay.');
        }

        journeyResetCount += 1;
        // notifyBot('RESETTING', 'Game Over detected → Resetting...', true);

        return; // Exit overlay handling
    }

    // ------------------------------------------------------------------
    // PHASE 2: OVERLAY IS HIDDEN (Main game loop running)
    // ------------------------------------------------------------------
    if (pendingZoneRestore) {
        const controls = getControls();

        if (controls) {
            if (pendingZoneRestore === 'toZone' && controls.toZone) {
                // Click to turn back on if currently off
                if (controls.toZone.classList.contains('off')) {
                    notifyBot('RESTORE', 'Restoring "To Zone" automation state...', false);
                    controls.toZone.click();
                }
            } else if (pendingZoneRestore === 'currentZone' && controls.currentZone) {
                // Click to turn back on if currently off
                if (controls.currentZone.classList.contains('off')) {
                    notifyBot('RESTORE', 'Restoring "Current Zone" automation state...', false);
                    controls.currentZone.click();
                }
            }
        }

        // Clear state so we don't re-trigger clicks every tick
        pendingZoneRestore = null;

        // notifyBot('RESTORE', 'Restoring zone automation state...', false);
    } else {
        notifyBot('ACTIVE', '', false);
    }
}

var journeyIntervalId;

/**
 * Stops the running automation loop.
 */
function tick_stop() {
    'use strict';
    if (journeyIntervalId) {
        clearInterval(journeyIntervalId);
        journeyIntervalId = null;
        notifyBot('STOPPED', 'Automation STOPPED.', true);
    }
}

/**
 * Starts the automation loop.
 * @param {number} [intervalMs=2000] How often to run (in milliseconds). Default 2000ms.
 */
function tick_start(intervalMs) {
    'use strict';
    var ms = typeof intervalMs === 'number'
        ? intervalMs
        : 2000;

    // Safety: always clear any existing interval so timers don't stack
    tick_stop();

    journeyIntervalId = setInterval(journey_tick, ms);
    notifyBot('STARTED', 'Automation STARTED (interval: ' + ms + 'ms). Call tick_stop() to halt.', false);
}

tick_start(1000);
