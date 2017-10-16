; Auto-generated. Do not edit!


(cl:in-package just_move-msg)


;//! \htmlinclude control.msg.html

(cl:defclass <control> (roslisp-msg-protocol:ros-message)
  ((control_message
    :reader control_message
    :initarg :control_message
    :type cl:string
    :initform "")
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass control (<control>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <control>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'control)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name just_move-msg:<control> is deprecated: use just_move-msg:control instead.")))

(cl:ensure-generic-function 'control_message-val :lambda-list '(m))
(cl:defmethod control_message-val ((m <control>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader just_move-msg:control_message-val is deprecated.  Use just_move-msg:control_message instead.")
  (control_message m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <control>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader just_move-msg:distance-val is deprecated.  Use just_move-msg:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <control>) ostream)
  "Serializes a message object of type '<control>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'control_message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'control_message))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <control>) istream)
  "Deserializes a message object of type '<control>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'control_message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'control_message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<control>)))
  "Returns string type for a message object of type '<control>"
  "just_move/control")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'control)))
  "Returns string type for a message object of type 'control"
  "just_move/control")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<control>)))
  "Returns md5sum for a message object of type '<control>"
  "f9d4f3ee22249204d59eaaa853bc7feb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'control)))
  "Returns md5sum for a message object of type 'control"
  "f9d4f3ee22249204d59eaaa853bc7feb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<control>)))
  "Returns full string definition for message of type '<control>"
  (cl:format cl:nil "string control_message~%float64 distance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'control)))
  "Returns full string definition for message of type 'control"
  (cl:format cl:nil "string control_message~%float64 distance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <control>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'control_message))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <control>))
  "Converts a ROS message object to a list"
  (cl:list 'control
    (cl:cons ':control_message (control_message msg))
    (cl:cons ':distance (distance msg))
))
