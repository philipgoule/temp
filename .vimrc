set number
let mapleader=','
call plug#begin('~/.vim/plugged')
Plug 'mhinz/vim-startify'
Plug 'vim-airline/vim-airline'
Plug 'Yggdroot/indentLine'
Plug 'scrooloose/nerdtree'
Plug 'w0ng/vim-hybrid'
Plug 'easymotion/vim-easymotion'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'vim-airline/vim-airline-themes'
Plug 'junegunn/fzf.vim'
Plug 'tpope/vim-surround'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'brooth/far.vim'
Plug 'python-mode/python-mode', { 'for': 'python', 'branch': 'develop' }
Plug 'majutsushi/tagbar'
Plug 'lfv89/vim-interestingwords'
Plug 'sbdchd/neoformat'
Plug 'w0rp/ale'
"pip  install pylint
if has('nvim')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
Plug 'deoplete-plugins/deoplete-jedi'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'junegunn/gv.vim'
let g:deoplete#enable_at_startup = 1
call plug#end()
"let g:neoformat_python_autopep8 = {
"            \ 'exe': 'autopep8',
"            \ 'args': ['-s 4', '-E'],
"            \ 'replace': 1 
"            \ 'stdin': 1, 
"            \ 'env': ["DEBUG=1"],
"	    \ 'valid_exit_codes': [0, 23],
"            \ 'no_append': 1,
"            \ }


set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
"Plugin 'ycm-core/YouCompleteMe'
" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

set background=dark
colorscheme hybrid
map <C-n> :NERDTreeToggle<CR>
map <C-n>f :NERDTreeFind<CR>
noremap <C-h> <C-w>h
noremap <C-j> <C-w>j
noremap <C-k> <C-w>k
noremap <C-l> <C-w>l
let NERDTreeShowHidden=1
nnoremap <leader>v :NERDTreeFind<cr>
let g:ctrlp_map = '<c-p>'
let g:ctrlp_show_hidden = 1
nmap ss <Plug>(easymotion-s2)
nnoremap <leader>t :TagbarToggle<cr>

"neoformat

let g:neoformat_enabled_python = ['autopep8']
