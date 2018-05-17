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
Currently, you have to start (and stop) the filewatcher, this can be automated
when you open a scala file:

```vim
autocmd BufRead *.scala :call MetalsFilewatcherStart()
```

to manually stop and start the file watcher you can do:

```vim
" start:
:call MetalsFilewatcherStart()

" and to stop:
:call MetalsFilewatcherStop()
```

## Future work
- Automatic start/stop of file-watching in `*.scala` files (this can currently be scripted in `init.vim`)
- Make sure that the plugin is only active if `LanguageClient-neovim` is installed
- Add watchers for other files than `*.semanticdb`, see
  [metals/docs/new-editor.md](https://github.com/scalameta/metals/blob/master/docs/new-editor.md#file-watching)
- Fix possible interferance with `deoplete`, not sure, have to investigate
