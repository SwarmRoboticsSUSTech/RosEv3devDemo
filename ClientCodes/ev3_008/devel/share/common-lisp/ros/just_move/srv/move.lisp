; Auto-generated. Do not edit!


(cl:in-package just_move-srv)


;//! \htmlinclude move-request.msg.html

(cl:defclass <move-request> (roslisp-msg-protocol:ros-message)
  ((control_message
    :reader control_message
    :initarg :control_message
    :type cl:string
    :initform ""))
)

(cl:defclass move-request (<move-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <move-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'move-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name just_move-srv:<move-request> is deprecated: use just_move-srv:move-request instead.")))

(cl:ensure-generic-function 'control_message-val :lambda-list '(m))
(cl:defmethod control_message-val ((m <move-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader just_move-srv:control_message-val is deprecated.  Use just_move-srv:control_message instead.")
  (control_message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <move-request>) ostream)
  "Serializes a message object of type '<move-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'control_message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'control_message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <move-request>) istream)
  "Deserializes a message object of type '<move-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'control_message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'control_message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<move-request>)))
  "Returns string type for a service object of type '<move-request>"
  "just_move/moveRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'move-request)))
  "Returns string type for a service object of type 'move-request"
  "just_move/moveRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<move-request>)))
  "Returns md5sum for a message object of type '<move-request>"
  "e3e06edf159d0eb6dd04caf49ff1b9fb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'move-request)))
  "Returns md5sum for a message object of type 'move-request"
  "e3e06edf159d0eb6dd04caf49ff1b9fb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<move-request>)))
  "Returns full string definition for message of type '<move-request>"
  (cl:format cl:nil "string control_message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'move-request)))
  "Returns full string definition for message of type 'move-request"
  (cl:format cl:nil "string control_message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <move-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'control_message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <move-request>))
  "Converts a ROS message object to a list"
  (cl:list 'move-request
    (cl:cons ':control_message (control_message msg))
))
;//! \htmlinclude move-response.msg.html

(cl:defclass <move-response> (roslisp-msg-protocol:ros-message)
  ((distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass move-response (<move-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <move-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'move-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name just_move-srv:<move-response> is deprecated: use just_move-srv:move-response instead.")))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <move-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader just_move-srv:distance-val is deprecated.  Use just_move-srv:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <move-response>) ostream)
  "Serializes a message object of type '<move-response>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <move-response>) istream)
  "Deserializes a message object of type '<move-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<move-response>)))
  "Returns string type for a service object of type '<move-response>"
  "just_move/moveResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'move-response)))
  "Returns string type for a service object of type 'move-response"
  "just_move/moveResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<move-response>)))
  "Returns md5sum for a message object of type '<move-response>"
  "e3e06edf159d0eb6dd04caf49ff1b9fb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'move-response)))
  "Returns md5sum for a message object of type 'move-response"
  "e3e06edf159d0eb6dd04caf49ff1b9fb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<move-response>)))
  "Returns full string definition for message of type '<move-response>"
  (cl:format cl:nil "float64 distance~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'move-response)))
  "Returns full string definition for message of type 'move-response"
  (cl:format cl:nil "float64 distance~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <move-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <move-response>))
  "Converts a ROS message object to a list"
  (cl:list 'move-response
    (cl:cons ':distance (distance msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'move)))
  'move-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'move)))
  'move-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'move)))
  "Returns string type for a service object of type '<move>"
  "just_move/move")