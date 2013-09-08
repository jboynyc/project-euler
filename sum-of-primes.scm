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
(define (sum-of-primes upto)
    (fold + 0 (filter prime? (range 2 upto))))

; get the sum of all primes below the number passed via the command line
(define (main args)
    (map print (map sum-of-primes (map string->number args))))

; run main when compiled with csc
(cond-expand
    ((and chicken compiling)
        (main (command-line-arguments)))
    (else #f))
