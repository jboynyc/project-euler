#!/usr/bin/env csi -ss

(use srfi-42)

(define (range from upto)
  (list-ec (:range n from upto) n))

(define (zero-length? l)
  (= (length l) 0))

(define (no-remainder? n d)
  (= (remainder n d) 0))

(define (rounded-sqrt n)
    (inexact->exact (round (sqrt n))))

(define (prime? x)
    (if (< x 2) 
        #f
        (zero-length? 
            (filter (lambda (i) (no-remainder? x i))
                    (range 2 (add1 (rounded-sqrt x)))))))

(define (nth-prime n #!optional (c 1) (p 2))
  (if (= c n) p
      (if (prime? (+ p 1)) (nth-prime n (+ c 1) (+ p 1))
                           (nth-prime n c (+ p 1)))))

; procedure main is run automatically by the interpreter 
; when invoked with the -ss option
(define (main args)
  (map print (map nth-prime (map string->number args))))

; run main when compiled with csc
(cond-expand
  ((and chicken compiling)
    (main (command-line-arguments)))
  (else #f))
