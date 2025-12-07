### LOAD COLORS
autoload -Uz colors && colors
setopt PROMPT_SUBST

# Initialize Starship
eval "$(starship init zsh)"

### INTERACTIVE SHELL CONFIG
if [[ $- == *i* ]]; then

    # QuickShell sequences
    if [[ -f ~/.local/state/quickshell/user/generated/terminal/sequences.txt ]]; then
        cat ~/.local/state/quickshell/user/generated/terminal/sequences.txt
    fi

    # Aliases
    alias pamcan="pacman"
    alias ls="eza --icons"
    alias dir="eza --icons"
    alias clear="printf '\033[2J\033[3J\033[1;1H'"
    alias q="qs -c ii"
fi
