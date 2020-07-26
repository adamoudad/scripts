;; Add white background to an image
;; Copy this script in ~/.config/GIMP/2.10/scripts
;; Then run "./add-background-color /path/to/your/image"
(define (add-background-color filename color)
  (let* ((image (car (gimp-file-load RUN-NONINTERACTIVE filename filename)))
	 (imageWidth (car (gimp-image-width image)))
	 (imageHeight (car (gimp-image-height image)))
	 (layer (car
		 (gimp-layer-new
		  image
		  imageWidth
		  imageHeight
		  RGB-IMAGE
		  "background"
		  100
		  LAYER-MODE-NORMAL)
		 )
		)
	 (top-layer (car (gimp-image-get-active-layer image)))
	 )
    (gimp-image-add-layer image layer 10)
    (cond ((equal? color "white")
	   (gimp-context-set-background '(255 255 255)))
	  ((equal? color "black")
	   (gimp-context-set-background '(0 0 0))))
    (gimp-drawable-fill layer BACKGROUND-FILL)
    (let ((result (car (gimp-image-merge-visible-layers image EXPAND-AS-NECESSARY))))
      (gimp-file-save RUN-NONINTERACTIVE image result "/home/adam/Tests/gimp-output.png" "")
      )
    (gimp-image-delete image)
    )
  )
;; (script-fu-menu-register "script-fu-add-background" "<Image>/File/Create/Text")
