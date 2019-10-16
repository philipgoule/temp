
(setq package-enable-at-startup nil)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(blink-cursor-blinks 1)
 '(blink-cursor-mode t)
 '(custom-set-faces nil)
 '(package-selected-packages (quote (helm-smex smex airline-themes ahungry-theme))))

(setq package-archives '(("gnu"   . "http://elpa.emacs-china.org/gnu/")
			 ("melpa" . "http://elpa.emacs-china.org/melpa/")))
(require 'package)
(package-initialize)
(load-theme 'ahungry t)
;;(require 'package)

;;(add-to-list 'package-archives '(“marmalade” . “http://marmalade-repo.org/packages/”) t)

;;(add-to-list 'package-archives '(“elpa” . “http://tromey.com/elpa/”) t)

;;(add-to-list 'package-archives '(“melpa” . “http://melpa.milkbox.net/packages/”) t)

;;(package-initialize)
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(require 'smex) ; Not needed if you use package.el
(smex-initialize) ; Can be omitted. This might cause a (minimal) delay
                    ; when Smex is auto-initialized on its first run.
(global-set-key (kbd "M-x") 'smex)
(global-set-key (kbd "M-X") 'smex-major-mode-commands)
;; This is your old M-x.
(global-set-key (kbd "C-c C-c M-x") 'execute-extended-command)

