#!/usr/bin/env sbcl --script
;;
;; common lisp version
;;
;; to test, use:
;;
;; $ brew install sbcl
;; $ chmod +x e2.lisp
;; $ ./e2.lisp
;;

(defun divides (x y)
  (= 0 (mod x y)))

(defun e2 (max_iter a b)
  (reduce #'+
    (loop for n from 1 to max_iter when (or (divides n a) (divides n b)) collect n)))

(pprint (e2 1000000 3 5))
