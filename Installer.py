# Version 0.1a

# Contributors
# ------------
# citr0net

# Ideas to implement:
# - 

import os
import sys
import subprocess
import fileinput
import shutil

username = os.getlogin()
userHomeDir = '/home/'+username+'/'
hyprlandDir = userHomeDir+'.config/hypr'
hyprDir = userHomeDir+'.config/hypr'
keybindsConf = hyprlandDir+'/hyprland/keybinds.conf'
keybindsCustomConf = hyprlandDir+'/custom/keybinds.conf'
fruityEnd4Path = hyprlandDir+'/fruity_end_4'
hypridleConf = hyprlandDir+'/hypridle.conf'

fruityEnd4File = fruityEnd4Path+'/fruityEnd4Base.conf'
# Create Files
os.system(f"mkdir -p '{fruityEnd4Path}'")
os.system(f'echo > "{fruityEnd4File}"')

os.system('clear')

def printTitle():
    print()
    print('''
   __            _ _                              _ _  _         _           _        _ _           
  / _|_ __ _   _(_) |_ _   _        ___ _ __   __| | || |       (_)_ __  ___| |_ __ _| | | ___ _ __ 
 | |_| '__| | | | | __| | | |_____ / _ \\ '_ \\ / _` | || |_      | | '_ \\/ __| __/ _` | | |/ _ \\ '__|
 |  _| |  | |_| | | |_| |_| |_____|  __/ | | | (_| |__   _|     | | | | \\__ \\ || (_| | | |  __/ |   
 |_| |_|   \\__,_|_|\\__|\\__, |      \\___|_| |_|\\__,_|  |_|       |_|_| |_|___/\\__\\__,_|_|_|\\___|_|   
                       |___/                                                                                                                                                                                                         
    ''')
    print()


whatToAddTofruityEnd4 = [
    '''
#   __            _ _                              _ _  _   
#  / _|_ __ _   _(_) |_ _   _        ___ _ __   __| | || |  
# | |_| '__| | | | | __| | | |_____ / _ \\ '_ \\ / _` | || |_ 
# |  _| |  | |_| | | |_| |_| |_____|  __/ | | | (_| |__   _|
# |_| |_|   \\__,_|_|\\__|\\__, |      \\___|_| |_|\\__,_|  |_|  
#                       |___/                                                   
#    ''',

]

whatToAddToCustomKeybinds = [
    '\n##! fruity-end4',
]

def fileOverwrite(filePath, toRewrite, replacementText):
    # FIX: Works with multi-line blocks instead of single-line matches
    if not os.path.exists(filePath):
        return

    with open(filePath, 'r') as f:
        content = f.read()  # FIX: read whole file so multi-line patterns can match

    # FIX: Replace full block, not per-line occurrences
    new_content = content.replace(toRewrite, replacementText)

    with open(filePath, 'w') as f:
        f.write(new_content)  # FIX: write full file back without truncation issues


def checkEnd4():
    checkerTmp = subprocess.run(['cat', '/home/'+username+'/.config/illogical-impulse/config.json'], capture_output=True)
    if checkerTmp != 'cat: /home/'+username+'/.config/illogical-impulse: No such file or directory':
        compatibility = True
        print('Check Completed')
    else:
        compatibility = False
        print('It does not appear you are running end-4 dot files.')
        print('Reason: the config file does not exist')
        input('Press enter to continue...')
        quit()

def fileAppend(filePath, appendText):
    with open(filePath, 'a') as file:
        file.write(appendText)

def getDiscordClientChoice():
    isValidChoice = 0
    while isValidChoice == 0:
        optionDiscordClient = int(input('''
What do you have installed:
1: Discord
2: Vesktop

Please type the coresponding number: '''))
        if optionDiscordClient == 1:
            isValidChoice == 1
            return 'Discord_clientTypeDiscord'
        elif optionDiscordClient == 2:
            isValidChoice = 1
            return 'Vesktop_clientTypeDiscord'
        else:
            isValidChoice = 0

def lookInFile(filePath, line):
    with open(filePath, 'r') as f:
        if line in f.read():
            return True
        else:
            return False

def chromiumBrowserFix():
    # Suggested by citr0net
    chromiumKeybindsDescription = '''
    \033[93mChromium Based Browser Crash Fix\033[00m
    If you use a chromium based browser, you might have noticed that the browser
    crashes when moving the browser to a different workspace. This patch will force
    all chromium based browsers (the ones under the keybinds file) to use X11 (or XWayland) 
    instead of Wayland, which fixes the issue at 0 compromise. This will also
    disable any firefox based browsers from being opened to the keybind, which
    is especially useful if you don't want to delete firefox, but it is preinstalled.

    Reccomended: Yes

    '''
    print(chromiumKeybindsDescription)
    toAddToCustom = '\nbind = Super, W, exec, ~/.config/hypr/hyprland/scripts/launch_first_available.sh "brave --ozone-platform=x11" "google-chrome-stable --ozone-platform=x11" "chromium --ozone-platform=x11" "microsoft-edge-stable --ozone-platform=x11" "opera --ozone-platform=x11" # Chromium Browser Patches\n'
    userInput = input('Would you like this patch? (Y/n): ')
    if userInput.lower() == 'n':
        print('Skipped!')
    else:
        fileOverwrite(keybindsConf, 
        'bind = Super, W, exec, ~/.config/hypr/hyprland/scripts/launch_first_available.sh "google-chrome-stable" "zen-browser" "firefox" "brave" "chromium" "microsoft-edge-stable" "opera" "librewolf" # Browser',
        '# bind = Super, W, exec, ~/.config/hypr/hyprland/scripts/launch_first_available.sh "brave" "google-chrome-stable" "zen-browser" "firefox" "brave" "chromium" "microsoft-edge-stable" "opera" "librewolf" # Browser -- Overwritten by fruityEnd4')
        print('Removed existing browser keybind')
        if not lookInFile(keybindsCustomConf, toAddToCustom):
            whatToAddToCustomKeybinds.append(toAddToCustom)
        else:
            print('Keybind already detected')


def applicationSpecialWorkspaces():
    # From citr0mods V1-3
    specialWorkspacesDescription = '''
    \033[93mSpecific Special Workspaces\033[00m
    If you've used the caelestia shell then you are very famillar with this one.
    It will give applications such as Discord / Vesktop and Spotify their own special
    workspace. Keybinds are overwriten and with 99% of updates, you will need to
    reinstall this script as keybinds can get overwritten. This will replace the built in
    special workspace function (Super + S). This will also autostart these applications

    Requires:
    - Spotify
    - Discord OR Vesktop

    Issues:
    - There is no way to tell if you opened the workspace if spotify or discord
      gets exited
    - Please help push this idea mainstream: 
      Link: https://github.com/end-4/dots-hyprland/issues/2196

    Reccomended: Depends
    '''
    print(specialWorkspacesDescription)
    userInput = input('Would you like this patch? (y/N): ')
    if userInput.lower() == 'y':
        conflictingKeybinds = {
        'bind = Super, D, fullscreen, 1 # Maximize': '# Feature conflicts with Discord / Vesktop - fruityEnd4', # Conflicts with Discord
        'bind = Super+Alt, S, movetoworkspacesilent, special # Send to scratchpad': '# Feature conflicts with Spotify - fruityEnd4', # Conflicts with spotify
        'bind = Ctrl+Super, S, togglespecialworkspace, # [hidden]': '# Feature conflicts with Spotify - fruityEnd4', # Conflicts with spotify
        'bind = Super, S, togglespecialworkspace, # Toggle scratchpad': '# Feature conflicts with Spotify - fruityEnd4' # Conflicts with spotify
        }

        for key, newKey in conflictingKeybinds.items():
            if lookInFile(keybindsCustomConf, key):
                fileOverwrite(keybindsConf, key, newKey)
                print('Rewriten Line that contains "',key+'" with "',newKey+'"')

        newKeybinds = [
            "\nbind = Super, S, togglespecialworkspace, spotify # Spotify Window",
            "\nbind = Super, D, togglespecialworkspace, discord # Discord Window"
        ]
        for key in newKeybinds:
            if not lookInFile(keybindsCustomConf, key):
                whatToAddToCustomKeybinds.append(key)

        if getDiscordClientChoice() == 'Discord_clientTypeDiscord':
            whatToAddTofruityEnd4.append('''\n
## Discord (Discord Client)
windowrulev2 = workspace special:discord, class:^(discord)$
workspace = special:discord, gapsout:30, on-startup:hide
exec-once = discord
                ''')
        else:
            whatToAddTofruityEnd4.append('''\n
## Discord (Discord Client)
windowrulev2 = workspace special:discord, class:^(vesktop)$
workspace = special:discord, gapsout:30, on-startup:hide
exec-once = vesktop
                ''')

        whatToAddTofruityEnd4.append('''\n
## Spotify
windowrulev2 = workspace special:spotify, class:^(Spotify)$
workspace = special:spotify, gapsout:30, on-startup:hide
exec-once = spotify
        ''')
    else:
        print('Skipped!')

def autoSizedApplications():
    autoSizedAppsDescription = '''
    \033[93mAutomanic Sized Applications\033[00m
    This will automanically size and float applications like Calculator Apps and Clock Apps.
    Useful as end-4 dot files do not do this by default.

    Supports:
    - Kcalc
    - Gnome Calculator
    - Gnome Clocks

    Reccomended: Yes
    '''
    print(autoSizedAppsDescription)
    userInput = input('Would you like this patch (Y/n): ')
    if userInput.lower() == 'n':
        print('Skipped!')
    else:
        newEntries = '''\n
## Floating Calculators
windowrulev2 = float, class:^(org.kde.kcalc)
windowrulev2 = float, class:^(org.gnome.Calculator)

## Auto Size Calculators:
windowrulev2 = size 472 473, class:^(org.kde.kcalc)
windowrulev2 = size 360 616, class:^(org.gnome.Calculator)

# Clocks
windowrulev2 = float, class:^(org.gnome.clocks)
windowrulev2 = size 457 545, class:^(org.gnome.clocks)
        '''

        whatToAddTofruityEnd4.append(newEntries)

def autoStartSteam():
    autoStartSteamDescription = '''
    \033[93mAuto-Start Steam\033[00m
    Self Explanitory. This starts steam on startup in the background.

    Requires:
    - Steam

    Reccomended: Yes

    '''
    print(autoStartSteamDescription)
    userInput = input('Would you like this patch? (Y/n): ')
    if userInput.lower() == 'n':
        print('Skipped!')
    else:
        whatToAddTofruityEnd4.append('''\n
## Auto Start Steam
exec-once = wait 5 && steam -silent''')

def mouseAcceleration():
    mouseAccelerationDescription = '''
    \033[93mDisable Mouse Acceleration\033[00m
    Self Explanitory. Disables mouse acceleration.
    Useful for gaming.

    Reccomended: Yes

    '''
    print(mouseAccelerationDescription)
    userInput = input('Would you like this patch? (Y/n): ')
    if userInput.lower() == 'n':
        print('Skipped!')
    else:
        whatToAddTofruityEnd4.append('''\n
        ## Disable Mouse Acceleration
input {
    sensitivity = 0
    accel_profile = flat
}
        ''')

def monitorPatches():
    monitorPatchesDescription = '''
    \033[93mMonitor Patches\033[00m
    This adds workspaces for every monitor. Especially useful for
    people with multiple monitors.

    Requires:
    - 2 or more displays

    Issues:
    - If you have ran this before, don't run it again.
      It will break things

    Reccomended: Depends

    '''
    print(monitorPatchesDescription)
    userChoice = input('Would you like this patch y/N? ')
    if userChoice.lower() == 'y':

        # --- FIX 1: Force hyprctl path & capture errors ---
        result = subprocess.run(
            ['/usr/bin/hyprctl', 'monitors'],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("ERROR: hyprctl failed to run.")
            return

        # --- FIX 2: Proper monitor name extraction ---
        # Hyprland output ALWAYS contains: "Monitor <name> (ID x)"
        monitors = []
        for line in result.stdout.splitlines():
            if line.startswith("Monitor"):
                # Example: "Monitor eDP-1 (ID 0):"
                parts = line.split()
                if len(parts) >= 2:
                    monitors.append(parts[1])

        if not monitors:
            print("ERROR: No monitors detected.")
            return

        # --- FIX 3: Ensure folder exists ---
        os.makedirs(fruityEnd4Path, exist_ok=True)

        monitorsFile = fruityEnd4Path + '/monitorAdditions.conf'

        # --- FIX 4: Ensure hyprland.conf gets the include line ---
        fileAppend(
            userHomeDir + '/.config/hypr/hyprland.conf',
            'source=' + monitorsFile
        )

        # --- FIX 5: Guaranteed file write ---
        try:
            with open(monitorsFile, "w") as f:
                workspace_count = 1
                for i, monitor in enumerate(monitors):
                    start_workspace = workspace_count
                    end_workspace = workspace_count + 9

                    f.write(
                        f"# --- Bind workspaces {start_workspace}-{end_workspace} "
                        f"(group {i+1}) to {monitor} ---\n"
                    )

                    for workspace in range(start_workspace, end_workspace + 1):
                        f.write(
                            f"workspace = {workspace}, monitor:{monitor}, default:true\n"
                        )

                    workspace_count = end_workspace + 1
        except Exception as e:
            print("ERROR: Failed to write monitorAdditions.conf:", e)
            return



def disableSleep():
    description = '''
    \033[93mDisable Sleep\033[00m
    Disables the automanic sleep feature, useful for desktops.
    Do not enable this on laptops!

    Requires:
    - Desktop

    Issues:
    - If you have ran this before, don't run it again.
      It will break things
    - Disabling this on laptops will have lower battery life!

    Reccomended: No

    '''
    print(description)
    userChoice = input('Would you like to apply this patch y/N: ')
    if userChoice.lower() == 'y':
        original = '''
listener {
    timeout = 900 # 15mins
    on-timeout = $suspend_cmd
}
'''
        new = '''
#listener {
#    timeout = 900 # 15mins
#    on-timeout = $suspend_cmd
#}
'''
        fileOverwrite(hypridleConf, original, new)

def addNewKeybinds():
    for key in whatToAddToCustomKeybinds:
        fileAppend(keybindsCustomConf, key)

    for key in whatToAddTofruityEnd4:
        fileAppend(fruityEnd4File, key)

printTitle()
checkEnd4()

entryAdditions = '''\n
# fruityEnd4
source=fruity_end_4/fruityEnd4Base.conf
'''
fileAppend(userHomeDir+'.config/hypr/hyprland.conf', entryAdditions)

chromiumBrowserFix()
applicationSpecialWorkspaces()
autoSizedApplications()
autoStartSteam()
mouseAcceleration()
monitorPatches()
disableSleep()

# Write to Disk
addNewKeybinds()

print('Your prefrences have been writen to disk!')
os.system('clear')
printTitle()
print('\nTo apply your changes, it is best to restart.')
choiceToRestart = input('Would you like to do that now? y/N: ')
if choiceToRestart == 'y':
    os.system('pkexec shutdown -r now')
