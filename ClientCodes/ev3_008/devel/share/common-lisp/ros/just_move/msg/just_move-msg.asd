
(cl:in-package :asdf)

(defsystem "just_move-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "control" :depends-on ("_package_control"))
    (:file "_package_control" :depends-on ("_package"))
  ))