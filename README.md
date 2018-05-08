# metals-filewatcher.nvim
This is a file watcher for the Scala
[metals](https://github.com/scalameta/metals) project.

## Installation
This plugin requires
[LanguageClient-neovim](https://github.com/autozimu/LanguageClient-neovim) to be
installed. As well as `watchdog` and `neovim` from pip3.

Watchdog and the neovim python lib can easily be installed with:

```bash
$ pip3 install neovim watchdog
```


The language client and the metals-filewatcher can be installed with:

```vim
Plug 'autozimu/LanguageClient-neovim', {
    \ 'branch': 'next',
    \ 'do': 'bash install.sh',
    \ }

Plug 'felixmulder/metals-filewatcher.nvim', { 'do': ':UpdateRemotePlugins' }
```

## Usage
Currently, you have to manually start (and stop) the filewatcher:

```
:call MetalsFilewatcherStart()
```

and

```
:call MetalsFilewatcherStop()
```

## Future work
- Automatic start/stop of file-watching in `*.scala` files (this can currently be scripted in `init.vim`)
- Making sure that the plugin is only active if `LanguageClient-neovim` is installed
