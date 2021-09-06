set nocompatible
filetype off

"=====================================================
" Vundle settings
"=====================================================
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'		" let Vundle manage Vundle, required

" color scheme
Plugin 'altercation/solarized'

" my plugins
Plugin 'tpope/vim-eunuch'
Plugin 'jiangmiao/auto-pairs'
Plugin 'preservim/nerdcommenter'
Plugin 'matze/vim-move'
Plugin 'ryanoasis/vim-devicons'
Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'
Plugin 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plugin 'junegunn/fzf.vim'
Plugin 'wincent/ferret'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'dense-analysis/ale'
Plugin 'sheerun/vim-polyglot'
Plugin 'tpope/vim-unimpaired'
Plugin 'frazrepo/vim-rainbow'
Plugin 'tommcdo/vim-exchange'
Plugin 'kana/vim-textobj-user'
Plugin 'kana/vim-textobj-entire'
Plugin 'vim-scripts/ReplaceWithRegister'
Plugin 'vim-scripts/argtextobj.vim'
Plugin 'goerz/jupytext.vim'

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" my plugins settings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" move
let g:move_key_modifier = 'C'

" NERDTree
let NERDTreeAutoDeleteBuffer = 1

" ale
let g:ale_linters = {'python': ['flake8', 'pylint']}
let g:ale_fixers = {
      \    'python': ['black'],
      \}
nmap <F10> :ALEFix<CR>
let g:ale_fix_on_save = 1

let g:snipMate = { 'snippet_version' : 1 }
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" my settings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap 2o o<CR>
nnoremap 2O O<Esc>O

" move tabs
nnoremap tm :tabm +1<CR>
nnoremap tM :tabm -1<CR>

" comments
map <C-?> <plug>NERDCommenterComment
map <C-_> <plug>NERDCommenterToggle

" font
set guifont=Ubuntu\ Mono\ 19

" wordwrap
"set textwidth=80
set linebreak

"---------=== Code/project navigation ===-------------
Plugin 'scrooloose/nerdtree' 	    	" Project and file navigation

"------------------=== Other ===----------------------
Plugin 'bling/vim-airline'   	    	" Lean & mean status/tabline for vim
Plugin 'fisadev/FixedTaskList.vim'  	" Pending tasks list
Plugin 'rosenfeld/conque-term'      	" Consoles as buffers
Plugin 'tpope/vim-surround'	   	" Parentheses, brackets, quotes, XML tags, and more

"--------------=== Snippets support ===---------------
Plugin 'garbas/vim-snipmate'		" Snippets manager
Plugin 'MarcWeber/vim-addon-mw-utils'	" dependencies #1
Plugin 'tomtom/tlib_vim'		" dependencies #2
Plugin 'honza/vim-snippets'		" snippets repo

"---------------=== Languages support ===-------------
" --- Python ---
Plugin 'maralla/completor.vim' " pip install jedi

call vundle#end()            		" required
filetype on
filetype plugin on
filetype plugin indent on

"=====================================================
" General settings
"=====================================================
set backspace=indent,eol,start
let no_buffers_menu=1
set mousemodel=popup

set ruler
set completeopt-=preview
set gcr=a:blinkon0
if has("gui_running")
  set cursorline
endif
set ttyfast

" включить подсветку кода
syntax on

tab sball
set switchbuf=useopen

" отключаем пищалку и мигание
set visualbell t_vb= 
set novisualbell       
autocmd GUIEnter * set vb t_vb=

set enc=utf-8	     " utf-8 по дефолту в файлах
set ls=2             " всегда показываем статусбар
set incsearch	     " инкреминтируемый поиск
set hlsearch	     " подсветка результатов поиска
set nu	             " показывать номера строк
set scrolloff=5	     " 5 строк при скролле за раз

" прячем панельки
"set guioptions-=m   " меню
set guioptions-=T    " тулбар
"set guioptions-=r   "  скроллбары

" настройка на Tab
set smarttab
set tabstop=8

" при переходе за границу в 80 символов в Ruby/Python/js/C/C++ подсвечиваем на темном фоне текст
"augroup vimrc_autocmds
"    autocmd!
"    autocmd FileType ruby,python,javascript,c,cpp highlight Excess ctermbg=DarkGrey guibg=Black
"    autocmd FileType ruby,python,javascript,c,cpp match Excess /\%80v.*/
"    autocmd FileType ruby,python,javascript,c,cpp set nowrap
"augroup END

" указываем каталог с настройками SnipMate
let g:snippets_dir = "~/.vim/vim-snippets/snippets"

" настройки Vim-Airline
set laststatus=2
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'

" NerdTree настройки
" показать NERDTree на F3
map <F3> :NERDTreeToggle<CR>
"игноррируемые файлы с расширениями
let NERDTreeIgnore=['\~$', '\.pyc$', '\.pyo$', '\.class$', 'pip-log\.txt$', '\.o$']

" TaskList настройки
map <F2> :TaskList<CR> 	   " отобразить список тасков на F2

" Работа буфферами
map <C-q> :bd<CR> 	   " CTRL+Q - закрыть текущий буффер

"=====================================================
" User hotkeys
"=====================================================
" ConqueTerm
" запуск интерпретатора на F5
nnoremap <F5> :ConqueTermSplit python<CR>
" а debug-mode на <F6>
nnoremap <F6> :exe "ConqueTermSplit python " . expand("%")<CR>
let g:ConqueTerm_StartMessages = 0
let g:ConqueTerm_CloseOnEnd = 0
" проверка кода в соответствии с PEP8 через <leader>8
autocmd FileType python map <buffer> <leader>8 :PymodeLint<CR>

" автокомплит через <Ctrl+Space>
inoremap <C-space> <C-x><C-o>

" переключение между синтаксисами
nnoremap <leader>Th :set ft=htmljinja<CR>
nnoremap <leader>Tp :set ft=python<CR>
nnoremap <leader>Tj :set ft=javascript<CR>
nnoremap <leader>Tc :set ft=css<CR>
nnoremap <leader>Td :set ft=django<CR>

"=====================================================
" Languages support
"=====================================================
" --- Python ---
autocmd FileType python setlocal expandtab shiftwidth=4 tabstop=8
\ formatoptions+=croq softtabstop=4 smartindent
\ cinwords=if,elif,else,for,while,try,except,finally,def,class,with
autocmd FileType pyrex setlocal expandtab shiftwidth=4 tabstop=8 softtabstop=4 smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class,with

" --- JavaScript ---
let javascript_enable_domhtmlcss=1
autocmd FileType javascript set omnifunc=javascriptcomplete#CompleteJS
autocmd BufNewFile,BufRead *.json setlocal ft=javascript

" --- HTML ---
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags

" --- template language support (SGML / XML too) ---
autocmd FileType html,xhtml,xml,htmldjango,htmljinja,eruby,mako setlocal expandtab shiftwidth=2 tabstop=2 softtabstop=2
autocmd bufnewfile,bufread *.rhtml setlocal ft=eruby
autocmd BufNewFile,BufRead *.mako setlocal ft=mako
autocmd BufNewFile,BufRead *.tmpl setlocal ft=htmljinja
autocmd BufNewFile,BufRead *.py_tmpl setlocal ft=python
let html_no_rendering=1
let g:sparkupNextMapping='<c-l>'

" --- CSS ---
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
autocmd FileType css setlocal expandtab shiftwidth=4 tabstop=4 softtabstop=4

set background=dark
colorscheme solarized

set wrap linebreak nolist

" open vimrc
nnoremap <F4> :tabe ~/.vimrc<CR>:tabm 0<CR>
set dictionary=/usr/share/dict/words
set spell

let g:jedi#goto_definitions_command = "<localleader>gg"
let g:rainbow_active = 1

se hidden
