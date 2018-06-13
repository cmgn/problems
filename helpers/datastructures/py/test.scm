(define reverse 
  (lambda (xs)
    (if (null? xs)
      '()
      (append (reverse (cdr xs)) (list (car xs))))))
