// prismatic_adventure_inject.js

// Global variable to store the timer reference
var botIntervalId = null;

/**
 * Stops the heartbeat timer.
 * startBot is much lower down, so it can call other functions
 */
function stopBot() {
    'use strict';
    if (botIntervalId !== null) {
        clearInterval(botIntervalId);
        botIntervalId = null;
        console.log('[JS Bot] Heartbeat stopped.');
    }
}

/**
 * Safely reads a JSON key from localStorage.
 * @param {string} key - The key to read.
 * @returns {Object|null} Parsed JSON data or null if invalid/missing.
 */
function loadStorageData(key) {
    'use strict';
    try {
        if (localStorage !== undefined && localStorage !== null) {
            var raw = localStorage.getItem(key);
            if (raw) {
                return JSON.parse(raw);
            }
        }
    } catch (err) {
        console.warn('[JS Bot] Failed to read from localStorage:', err);
    }
    return null;
}

/**
 * Safely writes a JSON value to localStorage.
 * @param {string} key - The key to write.
 * @param {Object} value - The object to serialize.
 */
function saveStorageData(key, value) {
    'use strict';
    try {
        if (localStorage !== undefined && localStorage !== null) {
            localStorage.setItem(key, JSON.stringify(value));
        }
    } catch (err) {
        console.warn('[JS Bot] Failed to write to localStorage:', err);
    }
}

var STORAGE_KEY_CONFIG = 'jsbot_config';
var STORAGE_KEY_TASKS = 'jsbot_taskAutoStore';
var STORAGE_KEY_RESOURCES = 'jsbot_resourceAutoStore';

// create, but do not initialize, local variables

var config;
var taskAutoStore;
var resourceAutoStore;

// save various storage

function saveConfig() {
    'use strict';
    saveStorageData(STORAGE_KEY_CONFIG, config);
}

function saveTasks() {
    'use strict';
    saveStorageData(STORAGE_KEY_TASKS, taskAutoStore);
}

function saveResources() {
    'use strict';
    saveStorageData(STORAGE_KEY_RESOURCES, resourceAutoStore);
}

// load various storage

function loadConfig() {
    'use strict';
    return loadStorageData(STORAGE_KEY_CONFIG);
}

function loadTasks() {
    'use strict';
    return loadStorageData(STORAGE_KEY_TASKS);
}

function loadResources() {
    'use strict';
    return loadStorageData(STORAGE_KEY_RESOURCES);
}

// 1. Initialize or load config
// Control variables to toggle auto-restart behavior
var default_config = {
    automate: 'OFF',             // 'OFF', 'Manual', 'zone', 'all'
    taskModeAuto: 'OFF',         // 'OFF', 'Normal', 'Travel', 'ALL'
    taskModeClearing: 'OFF',     // 'OFF', 'Normal', 'Travel', 'ALL'
    autoResources: true,
    autoRestartEnergy: true,
    autoRestartCopium: true,
    autoRestartDelusion: true,
    zzz_last: 0
};

var savedConfig = loadConfig();

if (!config) {
    if (savedConfig !== null && savedConfig !== undefined) {
        config = savedConfig;
    } else {
        config = default_config;
        saveConfig();
    }
}

// 2. Initialize or load task auto store
var savedTasks = loadTasks();

// Control variables for which items' checkboxes are checked
// Keys will be "zoneIdx_taskIdx", e.g., "4_8": true
if (!taskAutoStore) {
    if (savedTasks !== null && savedTasks !== undefined) {
        taskAutoStore = savedTasks;
    } else {
        taskAutoStore = {};
        saveTasks();
    }
}

// 3. Initialize or load resource auto store
var savedResources = loadResources();

if (!resourceAutoStore) {
    if (savedResources !== null && savedResources !== undefined) {
        resourceAutoStore = savedResources;
    } else {
        resourceAutoStore = {};
        saveResources();
    }
}

/**
 * Checks if an element is missing, hidden via CSS class, inline display, or visually detached.
 * @param {HTMLElement|string} target - The DOM element or string ID to check.
 * @returns {boolean} - True if hidden or missing, False if visible.
 */
function isElementHidden(target) {
    'use strict';

    const el = (
        (typeof target === 'string')
            ? document.getElementById(target)
            : target
    );

    if (!el) {
        return true;
    }

    return (
        el.classList.contains('hidden')
        || el.style.display === 'none'
        || el.offsetParent === null
    );
}

/**
 * Parses formatted game numbers with K/M/B/T suffixes into numeric values.
 * Handles uppercase, lowercase, and trailing characters cleanly.
 * @param {string} text - Raw string like "2.96K" or "12.5".
 * @returns {number} The numeric representation, or 0 if unparseable.
 */
function parseFormattedNumber(text) {
    'use strict';

    if (!text || typeof text !== 'string') {
        return 0;
    }

    // Strip commas and extra spaces, convert to uppercase for clean suffix matching
    var cleaned = text.replace(/,/g, '').trim().toUpperCase();
    var match = cleaned.match(/^([0-9.]+)\s*([A-Z])?/);

    if (!match) {
        var simpleFloat = parseFloat(cleaned);
        return isNaN(simpleFloat)
            ? 0
            : simpleFloat;
    }

    var baseValue = parseFloat(match[1]);
    var suffix = match[2] || '';

    if (isNaN(baseValue)) {
        return 0;
    }

    var multiplier = 1;
    if (suffix === 'K') {
        multiplier = 1000;
    } else if (suffix === 'M') {
        multiplier = 1000000;
    } else if (suffix === 'B') {
        multiplier = 1000000000;
    } else if (suffix === 'T') {
        multiplier = 1000000000000;
    }

    return Math.round(baseValue * multiplier);
}

/**
 * Enables smooth dragging on a target element via a header handle.
 * @param {Element} hudEl - The main HUD container element.
 * @param {Element} handleEl - The header element used as the drag handle.
 */
function makeHUDDraggable(hudEl, handleEl) {
    'use strict';

    if (!hudEl || !handleEl) {
        return;
    }

    var isDragging = false;
    var startX = 0;
    var startY = 0;
    var initialLeft = 0;
    var initialTop = 0;


    function onMouseMove(e) {
        if (!isDragging) {
            return;
        }

        var dx = e.clientX - startX;
        var dy = e.clientY - startY;

        hudEl.style.left = (initialLeft + dx) + 'px';
        hudEl.style.top = (initialTop + dy) + 'px';
    }

    function onMouseUp() {
        if (!isDragging) {
            return;
        }

        isDragging = false;
        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);
    }

    function onMouseDown(e) {
        // Ignore clicks on interactive controls inside the header
        var targetTag = e.target.tagName;
        if (targetTag === 'INPUT' || targetTag === 'BUTTON' || targetTag === 'SELECT') {
            return;
        }

        isDragging = true;
        startX = e.clientX;
        startY = e.clientY;

        // Get current computed position
        var rect = hudEl.getBoundingClientRect();
        initialLeft = rect.left;
        initialTop = rect.top;

        // Switch positioning from 'right' anchored to explicit 'left/top' pixel bounds
        hudEl.style.right = 'auto';
        hudEl.style.left = initialLeft + 'px';
        hudEl.style.top = initialTop + 'px';

        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
    }

    handleEl.addEventListener('mousedown', onMouseDown);
}

/**
 * Detects whether the active zone is a Clearing Zone (has "Full completes")
 * or an Automatable Zone.
 * @returns {string} 'clearing' or 'automatable'
 */
function getZoneType() {
    'use strict';

    // Inspect the DOM for the completion counter text
    var zoneHeader = document.querySelector('#zoneAutomation');
    if (zoneHeader) {
        if (zoneHeader.textContent.indexOf('Full Completes:') !== -1) {
            return 'clearing';
        }
        if (zoneHeader.querySelector('button') !== null) {
            return 'automatable';
        }
    }

    console.error('getZoneType: failed', zoneHeader);
    stopBot();
    return 'UNKNOWN';
}

/**
 * Updates HUD section highlights based on active zone type and returns
 * the active Task Mode for current processing.
 * @returns {string} Effective task mode ('OFF', 'Normal', 'Travel', 'ALL')
 */
function syncZoneUIAndGetTaskMode() {
    'use strict';

    var zoneType = getZoneType();
    var clearingGroup = document.getElementById('hud-group-clearing');
    var autoGroup = document.getElementById('hud-group-automatable');

    var clearingTaskSelect = document.getElementById('hud-task-mode-clearing');
    var autoTaskSelect = document.getElementById('hud-task-mode-auto');

    if (zoneType === 'clearing') {
        if (autoGroup) {
            autoGroup.classList.remove('hud-active-group');
        }
        if (clearingGroup) {
            clearingGroup.classList.add('hud-active-group');
        }

        return config.taskModeClearing || (
            clearingTaskSelect
                ? clearingTaskSelect.value
                : 'OFF'
        );
    }

    // Default to Automatable Zone
    if (clearingGroup) {
        clearingGroup.classList.remove('hud-active-group');
    }
    if (autoGroup) {
        autoGroup.classList.add('hud-active-group');
    }

    return config.taskModeAuto || (
        autoTaskSelect
            ? autoTaskSelect.value
            : 'OFF'
    );
}

function create_HUD_object() {
    'use strict';

    var HUD_VERSION = '1.9';

    // Prevent duplicate HUD creation
    var existingHud_A = document.getElementById('jsbot-hud');
    var existingHud_B = document.getElementById('prismatic-bot-hud');
    var existingHud = existingHud_A || existingHud_B;

    if (existingHud) {
        var oldVersion = existingHud.getAttribute('data-version') || 'unknown';

        // Check if existing HUD version matches current version
        if (oldVersion === HUD_VERSION) {
            return existingHud;
        }
        // Remove outdated HUD instance to force re-render
        console.log('[JS Bot] Replacing obsolete HUD version ' + oldVersion + ' -> ' + HUD_VERSION);
        existingHud.parentNode.removeChild(existingHud);
        // now fall through to re-create a new copy
    }

    var hud = document.createElement('div');
    hud.id = 'prismatic-bot-hud';
    hud.setAttribute('data-version', HUD_VERSION);

    hud.innerHTML =
            '<div class="hud-header">' +
            '    <span>Prismatic Bot</span>' +
            '    <span class="hud-version">v' + HUD_VERSION + '</span>' +
            '</div>' +

            // 1. Clearing Zone Controls
            '<fieldset class="hud-zone-group" id="hud-group-clearing">' +
            '    <legend>Clearing Zone Controls</legend>' +
            '    <div class="hud-row disabled-row">' +
            '        <span>Automation:</span>' +
            '        <span class="hud-disabled-tag">N/A (Clearing)</span>' +
            '    </div>' +
            '    <div class="hud-row">' +
            '        <label><span>Clearing Tasks:</span>' +
            '            <select id="hud-task-mode-clearing">' +
            '                <option value="OFF">OFF</option>' +
            '            <option value="Normal">Normal</option>' +
            '            <option value="Travel">Travel</option>' +
            '            <option value="ALL">ALL</option>' +
            '        </select>' +
            '    </label>' +
            '    </div>' +
            '</fieldset>' +

            // 2. Automatable Zone Controls
            '<fieldset class="hud-zone-group" id="hud-group-automatable">' +
            '    <legend>Automated Zone Controls</legend>' +
            '    <div class="hud-row">' +
            '        <label><span>Automation:</span>' +
            '            <select id="hud-automate">' +
            '            <option value="OFF">OFF</option>' +
            '            <option value="zone">Zone</option>' +
            '            <option value="all">All</option>' +
            '                <option value="manual">Manual</option>' +
            '            </select>' +
            '        </label>' +
            '    </div>' +

            '    <div class="hud-row">' +
            '        <label><span>Auto Tasks:</span>' +
            '            <select id="hud-task-mode-auto">' +
            '                <option value="OFF">OFF</option>' +
            '                <option value="Normal">Normal</option>' +
            '                <option value="Travel">Travel</option>' +
            '                <option value="ALL">ALL</option>' +
            '            </select>' +
            '        </label>' +
            '    </div>' +
            '</fieldset>' +

            '<div class="hud-stats-group">' +
            '    <div class="hud-row">' +
            '        <label for="hud-auto-resources">' +
            '            <span>Use Resources:</span>' +
            '            <input type="checkbox" id="hud-auto-resources">' +
            '        </label>' +
            '    </div>' +
            '    <div class="hud-stat-row">' +
            '        <span>Max Energy:</span>' +
            '        <span id="hud-max-energy" class="hud-stat-value">--</span>' +
            '    </div>' +
            '</div>' +

            '<fieldset class="game-over-group">' +
            '    <legend>Game Over Restarts</legend>' +
            '    <div class="hud-row">' +
            '        <label><span>Restart Energy:</span><input type="checkbox" id="hud-auto-restart-energy"></label>' +
            '    </div>' +
            '    <div class="hud-row">' +
            '        <label><span>Restart Copium:</span><input type="checkbox" id="hud-auto-restart-copium"></label>' +
            '    </div>' +
            '    <div class="hud-row">' +
            '        <label><span>Restart Delusion:</span><input type="checkbox" id="hud-auto-restart-delusion"></label>' +
            '    </div>' +
            '</fieldset>';

    return hud;
}

function bindHUDEvents() {
    'use strict';

    var automateSelect = document.getElementById('hud-automate');
    if (automateSelect) {
        automateSelect.value = config.automate;
        automateSelect.addEventListener('change', function (e) {
            config.automate = e.target.value;
            console.log('[JS Bot] Automation mode set to: ' + config.automate);
            saveConfig();
        });
    }

    var taskAutoSelect = document.getElementById('hud-task-mode-auto');
    if (taskAutoSelect) {
        taskAutoSelect.value = config.taskModeAuto;
        taskAutoSelect.addEventListener('change', function (e) {
            config.taskModeAuto = e.target.value;
            console.log('[JS Bot] Automation Task Mode set to: ' + config.taskMode);
            saveConfig();
        });
    }

    var taskClearingSelect = document.getElementById('hud-task-mode-clearing');
    if (taskClearingSelect) {
        taskClearingSelect.value = config.taskModeClearing;
        taskClearingSelect.addEventListener('change', function (e) {
            config.taskModeClearing = e.target.value;
            console.log('[JS Bot] Clearing Task Mode set to: ' + config.taskMode);
            saveConfig();
        });
    }


    var autoResourcesCheckbox = document.getElementById('hud-auto-resources');
    if (autoResourcesCheckbox) {
        autoResourcesCheckbox.checked = config.autoResources;
        autoResourcesCheckbox.addEventListener('change', function (e) {
            config.autoResources = e.target.checked;
            saveConfig();
            console.log('[JS Bot] Use Resources set to: ' + config.autoResources);
        });
    }

    var energyCheckbox = document.getElementById('hud-energy');
    if (energyCheckbox) {
        energyCheckbox.checked = config.autoRestartEnergy;
        energyCheckbox.addEventListener('change', function (e) {
            config.autoRestartEnergy = e.target.checked;
            saveConfig();
            console.log('[JS Bot] Auto Restart Energy set to: ' + config.autoRestartEnergy);
        });
    }

    var copiumCheckbox = document.getElementById('hud-copium');
    if (copiumCheckbox) {
        copiumCheckbox.checked = config.autoRestartCopium;
        copiumCheckbox.addEventListener('change', function (e) {
            config.autoRestartCopium = e.target.checked;
            saveConfig();
            console.log('[JS Bot] Auto Restart Copium set to: ' + config.autoRestartCopium);
        });
    }

    var autoRestartDelusionCheckbox = document.getElementById('hud-auto-restart-delusion');
    if (autoRestartDelusionCheckbox) {
        autoRestartDelusionCheckbox.checked = config.autoRestartDelusion;
        autoRestartDelusionCheckbox.addEventListener('change', function (e) {
            config.autoRestartDelusion = e.target.checked;
            saveConfig();
            console.log('[JS Bot] Auto Restart Delusion set to: ' + config.autoRestartDelusion);
        });
    }
}

/**
 * Injects a floating HUD control panel into the page.
 */
function createHUD() {
    'use strict';

    var hud = create_HUD_object();
    document.body.appendChild(hud);
    var header = hud.querySelector('.hud-header');
    makeHUDDraggable(hud, header);

    bindHUDEvents();
}

/**
 * Decorates a single task element with an auto-run checkbox.
 * @param {Element} taskEl - The DOM element representing the task.
 */
function decorateTaskElement(taskEl) {
    'use strict';

    var zoneIdx = taskEl.getAttribute('data-zone-index');
    var taskIdx = taskEl.getAttribute('data-task-index');

    if (zoneIdx === null || taskIdx === null) {
        return;
    }

    var taskKey = zoneIdx + '_' + taskIdx;

    // Check if checkbox control already exists
    if (taskEl.querySelector('.jsbot-task-checkbox')) {
        return;
    }

    var computedView = document.defaultView || taskEl.ownerDocument.defaultView;
    if (computedView && computedView.getComputedStyle(taskEl).position === 'static') {
        taskEl.style.position = 'relative';
    }

    var label = document.createElement('label');
    label.className = 'jsbot-task-label';
    label.style.cssText =
            'position: absolute;' +
            'top: 4px;' +
            'right: 6px;' +
            'z-index: 100;' +
            'font-size: 10px;' +
            'color: #4af;' +
            'background: rgba(0,0,0,0.6);' +
            'padding: 1px 4px;' +
            'border-radius: 3px;' +
            'cursor: pointer;' +
            'user-select: none;';

    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'jsbot-task-checkbox';
    checkbox.style.cssText = 'margin-right: 3px; vertical-align: middle;';

    // Restore previous stored state if it exists
    if (taskAutoStore[taskKey] === true) {
        checkbox.checked = true;
    }
    checkbox.addEventListener('change', function (e) {
        taskAutoStore[taskKey] = e.target.checked;
        saveTasks();
        console.log('[JS Bot] Task [' + taskKey + '] auto-run set to: ' + e.target.checked);
    });

    label.appendChild(checkbox);
    label.appendChild(document.createTextNode('auto'));
    taskEl.appendChild(label);
}

/**
 * Scans for tasks in the DOM and injects/syncs auto-run checkboxes.
 */
function syncTaskCheckboxes() {
    'use strict';

    var tasks = document.querySelectorAll('#tasks .task');

    Array.prototype.forEach.call(tasks, function (taskEl) {
        decorateTaskElement(taskEl);
    });
}

/**
 * Decorates a single resource DOM element with an auto-consume checkbox.
 * @param {Element} resEl - The resource element.
 */
function decorateResourceElement(resEl) {
    'use strict';

    // Identify resource by data attribute, id, or fallback
    var resKey = (
        resEl.getAttribute('data-resource')
        || resEl.getAttribute('data-name')
        || resEl.id
    );

    if (!resKey) {
        return;
    }

    if (resEl.querySelector('.jsbot-resource-checkbox')) {
        return;
    }

    var computedView = document.defaultView || resEl.ownerDocument.defaultView;
    if (computedView && computedView.getComputedStyle(resEl).position === 'static') {
        resEl.style.position = 'relative';
    }

    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'jsbot-resource-checkbox';
    checkbox.style.cssText =
            'position: absolute;' +
            'top: 2px;' +
            'right: 2px;' +
            'z-index: 100;' +
            'cursor: pointer;' +
            'margin: 0;';

    if (resourceAutoStore[resKey] === true) {
        checkbox.checked = true;
    }

    checkbox.addEventListener('change', function (e) {
        resourceAutoStore[resKey] = e.target.checked;
        saveResources();
        console.log('[JS Bot] Resource [' + resKey + '] auto-consume set to: ' + e.target.checked);
    });

    // Prevent clicking the checkbox from triggering the underlying resource click
    checkbox.addEventListener('click', function (e) {
        e.stopPropagation();
    });

    resEl.appendChild(checkbox);
}

/**
 * Scans for resource elements in the DOM and injects auto-consume checkboxes.
 */
function syncResourceCheckboxes() {
    'use strict';

    var resources = document.querySelectorAll('#resourcesGrid .resource-item, #resources .resource-item, .resource-node');

    Array.prototype.forEach.call(resources, function (resEl) {
        decorateResourceElement(resEl);
    });
}

/**
 * Dispatches a synthetic contextmenu (right-click) event to a target DOM node.
 * Uses strict dynamic references to satisfy global-variable linters.
 * @param {Element} element - The target DOM element.
 */
function triggerRightClick(element) {
    'use strict';

    if (!element || !element.ownerDocument) {
        return;
    }

    var doc = element.ownerDocument;
    var return_this = function () {
        return this;
    };
    var view = doc.defaultView || return_this();
    var evt;

    if (view && typeof view.MouseEvent === 'function') {
        evt = new view.MouseEvent('contextmenu', {
            bubbles: true,
            cancelable: true,
            view: view,
            button: 2,
            buttons: 2
        });
    } else if (doc.createEvent) {
        evt = doc.createEvent('MouseEvents');
        evt.initMouseEvent(
            'contextmenu',
            true,   // bubbles
            true,   // cancelable
            view,   // view
            1,      // detail
            0,      // screenX
            0,      // screenY
            0,      // clientX
            0,      // clientY
            false,  // ctrl
            false,  // alt
            false,  // shift
            false,  // meta
            2,      // button (right click)
            null    // relatedTarget
        );
    }

    if (evt) {
        element.dispatchEvent(evt);
    }
}

/**
 * Predicate to determine if a resource is executable.
 * @param {Element} resEl - The resource element.
 * @returns {boolean} True if eligible to be consumed.
 */
function isResourceExecutable(resEl) {
    'use strict';

    if (!config.autoResources || isElementHidden(resEl)) {
        return false;
    }

    var resKey = (
        resEl.getAttribute('data-resource')
        || resEl.getAttribute('data-name')
        || resEl.id
    );

    if (!resKey || resourceAutoStore[resKey] !== true) {
        return false;
    }

    return true;
}

/**
 * Automates right-clicking checked, available resources.
 * @returns {boolean} True if a resource was right-clicked, false otherwise.
 */
function processAutomatedResources() {
    'use strict';

    if (!config.autoResources) {
        return false;
    }

    var resources = document.querySelectorAll('#resourcesGrid .resource-item, #resources .resource-item, .resource-node');
    var executableResources = Array.prototype.filter.call(resources, isResourceExecutable);

    if (executableResources.length === 0) {
        return false;
    }

    var targetRes = executableResources[0];
    var resKey = (
        targetRes.getAttribute('data-resource')
        || targetRes.getAttribute('data-name')
        || targetRes.id
    );

    triggerRightClick(targetRes);
    console.log('[JS Bot] Right-clicked automated resource [' + resKey + ']');
    return true;
}

/**
 * Retrieves all task DOM elements as a true JavaScript Array.
 * @returns {Array<Element>} Array of task elements.
 */
function getTaskElements() {
    'use strict';
    var nodes = document.querySelectorAll('#tasks .task');
    return Array.from(nodes);
}

/**
 * Determines whether a task element is a zone travel task.
 * @param {Element} taskEl - The task element to check.
 * @returns {boolean} True if it is a travel task, false otherwise.
 */
function isTravelTask(taskEl) {
    'use strict';
    return taskEl.classList.contains('travel-task');
}

/*
 * Helper predicates: do what they say on the tin
 */
function isTaskEnabledInConfig(taskEl, activeTaskMode) {
    'use strict';

    // Master switch OFF
    if (activeTaskMode === 'OFF') {
        return false;
    }

    var travel = isTravelTask(taskEl);

    // Normal mode: reject travel tasks
    if (activeTaskMode === 'Normal' && travel) {
        return false;
    }

    // Travel mode: reject normal (non-travel) tasks
    if (activeTaskMode === 'Travel' && !travel) {
        return false;
    }

    // Hidden (=== done already)
    if (isElementHidden(taskEl)) {
        return false;
    }

    // Verify Checkbox for Task is Checked
    var zoneIdx = taskEl.getAttribute('data-zone-index');
    var taskIdx = taskEl.getAttribute('data-task-index');

    if (zoneIdx === null || taskIdx === null) {
        return false;
    }

    var taskKey = zoneIdx + '_' + taskIdx;

    if (taskAutoStore[taskKey] !== true) {
        return false;
    }

    return true;
}

function isTaskGrayedOut(taskEl) {
    'use strict';
    var button = taskEl.querySelector('.task-control button');
    return (!button || button.disabled);
}

function isTaskInProgress(taskEl) {
    'use strict';
    var button = taskEl.querySelector('.task-control button');
    return (!button || button.classList.contains('active'));
}

/*
 * Helper functions: same comment
 */
function triggerClick(targetTask) {
    'use strict';
    var button = targetTask.querySelector('.task-control button');
    button.click();
}

function getTaskName(targetTask) {
    'use strict';
    var zoneIdx = targetTask.getAttribute('data-zone-index');
    var taskIdx = targetTask.getAttribute('data-task-index');
    return (zoneIdx + '_' + taskIdx);
}

/**
 * Automates execution for checked, available tasks.
 * Processes automated tasks sequentially, ensuring normal tasks complete fully
 * before initiating a Travel task.
 * @returns {boolean} True if a task click was performed, false otherwise.
 */
function processAutomatedTasks(activeTaskMode) {
    'use strict';

    if (activeTaskMode === 'OFF') {
        return false;
    }

    // 1. Get all task elements
    var taskElements = getTaskElements();
    if (!taskElements || taskElements.length === 0) {
        return false;
    }

    // 2. Filter eligible tasks (checked in HUD & available)
    var eligibleTasks = taskElements.filter(function (el, activeTaskMode) {
        return isTaskEnabledInConfig(el, activeTaskMode) && !isTaskGrayedOut(el);
    });
    if (eligibleTasks.length === 0) {
        return false;
    }

    // 3. Check if any normal (non-travel) tasks are still pending or in-progress
    var hasIncompleteNormalTasks = eligibleTasks.some(function (el) {
        return !isTravelTask(el);
    });

    // 4. Filter out tasks that are already running
    var readyTasks = eligibleTasks.filter(function (el) {
        return !isTaskInProgress(el);
    });
    if (readyTasks.length === 0) {
        return false;
    }

    // 5. Sort normal tasks first, travel tasks last
    var boolean_integer = function (x) {
        return (
            x
                ? 1
                : 0
        );
    };
    var normal_before_travel = function (a, b) {
        return (
            0
            + boolean_integer(isTravelTask(a))
            - boolean_integer(isTravelTask(b))
        );
    };
    readyTasks.sort(normal_before_travel);

    // 6. Pick top candidate
    var targetTask = readyTasks[0];

    // 7. Guard Travel: hold off if any normal task is still running or pending
    if (isTravelTask(targetTask) && hasIncompleteNormalTasks) {
        return false;
    }

    // 8. Execute click
    triggerClick(targetTask);

    console.log('[JS Bot] Executed task [' + getTaskName(targetTask) + ']');

    return true;
}

/**
 * Helper function to check visibility, click a button, and log output.
 * @param {string} containerId - The ID of the container element to check.
 * @param {string} buttonId - The ID of the restart button to click.
 * @param {boolean} isEnabled - The control variable enabling this check.
 * @param {string} logMessage - Message to log upon clicking.
 * @returns {boolean} - True if clicked, False otherwise.
 */
function handleAutoRestart(containerId, buttonId, isEnabled, logMessage) {
    'use strict';

    if (!isEnabled) {
        return false;
    }

    const container = document.getElementById(containerId);
    if (!container) {
        return false;
    }

    // Check if hidden via inline style or CSS class
    const isHidden = isElementHidden(container);

    if (isHidden) {
        return false;
    }

    const restartBtn = document.getElementById(buttonId);

    if (!restartBtn) {
        return false;
    }

    restartBtn.click();
    console.log(`[JS Bot] ${logMessage}`);

    return true;
}

// Function 1: Check & Restart for Energy Game Over
function checkAndRestartEnergy() {
    'use strict';

    return handleAutoRestart(
        'gameOverContentEnergy',
        'restartButtonEnergy',
        config.autoRestartEnergy,
        'Energy Game Over detected. Clicking Restart.'
    );
}

// Function 2: Check & Restart for Copium Game Over
function checkAndRestartCopium() {
    'use strict';

    return handleAutoRestart(
        'gameOverContentCopium',
        'restartButtonCopium',
        config.autoRestartCopium,
        'Copium Game Over detected. Clicking Restart.'
    );
}

// Function 3: Check & Restart for Delusion Game Over
/**
 * Automatically clicks the restart button on the Delusion Game Over screen when active.
 * @returns {boolean} True if a restart action was triggered, false otherwise.
 */
function checkAndRestartDelusion() {
    'use strict';

    return handleAutoRestart(
        'gameOverContentDelusion',
        'restartButtonDelusion',
        config.autoRestartDelusion,
        'Delusion Game Over detected. Clicking Restart.'
    );
}

/**
 * Ensures the specified automation button is active if present.
 * @returns {boolean} - True if an action was taken, False if target state was already met or elements missing.
 */
function setZoneAutomation() {
    'use strict';
    var container = document.getElementById('zoneAutomation');

    // 1. In clearing zones, zone automation buttons don't exist: exit early
    if (getZoneType() === 'clearing') {
        return false;
    }

    // Guard clause: check container existence and visibility
    if (isElementHidden(container)) {
        return false;
    }

    // In 'manual' mode, do not manipulate automation buttons.
    if (config.automate === 'manual') {
        return false;
    }

    var zoneBtn = container.querySelector('button[data-automation="zone"]');
    var allBtn = container.querySelector('button[data-automation="all"]');

    // Guard clause: confirm buttons exist
    if (!zoneBtn || !allBtn) {
        return false;
    }

    var targetMode = config.automate;

    if (targetMode === 'zone' && !zoneBtn.classList.contains('active')) {
        zoneBtn.click();
        console.log('[JS Bot] Set automation to: Zone');
        return true;
    }

    if (targetMode === 'all' && !allBtn.classList.contains('active')) {
        allBtn.click();
        console.log('[JS Bot] Set automation to: All');
        return true;
    }

    if (targetMode === 'OFF') {
        if (zoneBtn.classList.contains('active')) {
            zoneBtn.click();
            console.log('[JS Bot] Disabled Zone automation');
            return true;
        }
        if (allBtn.classList.contains('active')) {
            allBtn.click();
            console.log('[JS Bot] Disabled All automation');
            return true;
        }
    }

    return false; // No action needed/taken
}

/**
 * Reads and parses the maximum energy capacity from the EnergyBar tooltip attribute.
 * @returns {number|null} Max energy capacity, or null if missing/unparseable.
 */
function getMaxEnergy() {
    'use strict';
    var energyBar = document.getElementById('energyBar');
    if (!energyBar) {
        return null;
    }

    var tooltip = energyBar.getAttribute('data-tooltip') || '';
    if (!tooltip || tooltip.indexOf('/') === -1) {
        return null;
    }

    // Tooltip format expected: "Current / Max" (e.g., "1.2K/2.96K" or "1200/2960")
    // var match = tooltip.match(/Energy:\s*[\d.]+\/([\d.]+)/);
    var parts = tooltip.split('/');
    var maxStr = parts[1]
        ? parts[1].trim()
        : '';

    var numericMax = parseFormattedNumber(maxStr);
    return numericMax > 0
        ? numericMax
        : null;
}

/**
 * Updates the read-only Max Energy value in the HUD.
 */
function updateHUDStats() {
    'use strict';
    var maxEnergy = getMaxEnergy();
    var displayEl = document.getElementById('hud-max-energy');

    if (displayEl) {
        displayEl.textContent = (
            (maxEnergy !== null)
                ? maxEnergy
                : '--'
        );
    }
}

/**
 * Main execution tick.
 * Calls all modular checks sequentially.
 */
function run() {
    'use strict';

    // Always run per-tick visual syncs
    updateHUDStats();
    syncTaskCheckboxes();
    syncResourceCheckboxes();
    var activeTaskMode = syncZoneUIAndGetTaskMode();

    // Execute first successful action and short-circuit remainder
    return (
        checkAndRestartEnergy()
        || checkAndRestartCopium()
        || checkAndRestartDelusion()
        || processAutomatedResources()
        || setZoneAutomation()
        || processAutomatedTasks(activeTaskMode)
        // Future modular checks can be added here
    );
}

/**
 * Starts the heartbeat timer.
 * stopBot is much higher up, so other functions can call it
 * @param {number} intervalMs - Milliseconds between ticks (default: 1000).
 */
function startBot(intervalMs) {
    'use strict';
    // Clear any existing timer to prevent running duplicate loops
    if (botIntervalId !== null) {
        clearInterval(botIntervalId);
    }

    botIntervalId = setInterval(run, intervalMs);
    console.log(`[JS Bot] Heartbeat started (${intervalMs}ms interval).`);
}

// Initialize HUD and start heartbeat loop on script injection
createHUD();
startBot(1000);

function dont_complain() {
    'use strict';
    // run();
    stopBot();
    dont_complain();
}
