set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'acmpo6ou/vim-emoji-ab'
Plugin 'tpope/vim-surround'
Plugin 'matze/vim-move'
Plugin 'tpope/vim-unimpaired'
Plugin 'tommcdo/vim-exchange'
Plugin 'kana/vim-textobj-user'
Plugin 'kana/vim-textobj-entire'
Plugin 'vim-scripts/ReplaceWithRegister'
Plugin 'vim-scripts/argtextobj.vim'
Plugin 'preservim/nerdcommenter'

"""""" my plugins settings

" move
let g:move_key_modifier = 'C'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

nn 2o o<CR>
nn 2O O<Esc>O
map zz <Cmd>SVPress <LT>C-M-S-D-l><CR>

" comments
map <C-?> <plug>NERDCommenterComment
map <C-_> <plug>NERDCommenterToggle

runtime macros/emoji-ab.vim
