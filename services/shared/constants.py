# ════════════════════════════════
# RabbitMQ
# ════════════════════════════════
RABBITMQ_EXCHANGE = "booking_events"
RABBITMQ_EXCHANGE_TYPE = "topic"

# ════════════════════════════════
# Routing keys (publishers use these)
# ════════════════════════════════
EVENT_BOOKING_CONFIRMED  = "booking.confirmed"
EVENT_BOOKING_REQUESTED  = "booking.requested"
EVENT_BOOKING_DECLINED   = "booking.declined"
EVENT_BOOKING_EXPIRED    = "booking.expired"
EVENT_PAYMENT_SUCCESS    = "payment.success"
EVENT_PAYMENT_HELD       = "payment.held"
EVENT_PAYMENT_ERROR      = "payment.error"
EVENT_DEPOSIT_RESOLVED   = "deposit.resolved"

# ════════════════════════════════
# Booking statuses
# ════════════════════════════════
STATUS_AWAITING_PAYMENT  = "AWAITING_PAYMENT"
STATUS_CONFIRMED         = "CONFIRMED"
STATUS_FAILED_PAYMENT    = "FAILED_PAYMENT"
STATUS_PAID              = "PAID"
STATUS_PENDING_HOST      = "PENDING_HOST"
STATUS_REJECTED          = "REJECTED"
STATUS_EXPIRED           = "EXPIRED"

# ════════════════════════════════
# Payment transaction types
# ════════════════════════════════
TXN_BOOKING_CAPTURE      = "BOOKING_PAYMENT_CAPTURE"
TXN_BOOKING_AUTHORIZE    = "BOOKING_PAYMENT_AUTHORIZE"

# ════════════════════════════════
# Deposit actions
# ════════════════════════════════
DEPOSIT_RELEASE          = "RELEASE"
DEPOSIT_CAPTURE          = "CAPTURE"
DEPOSIT_AUTO_RELEASE     = "AUTO_RELEASE"

# ════════════════════════════════
# Deposit reasons
# ════════════════════════════════
REASON_HOST_REPORT       = "HOST_REPORT"
REASON_DAMAGE            = "DAMAGE"
REASON_NO_REPORT_48HR    = "NO_REPORT_48HR"