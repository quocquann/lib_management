BOOK_COPY_STATUS = (("a", "Available"), ("b", "Borrowed"))

REQUEST_STATUS = (("pending", "pending"), ('rejected', "rejected"), ("approved", "approved"))
DEFAULT_REQUEST_STATUS = "pending"

REQUEST_TYPE = (("borrow", "Borrow"), ("renew", "Renew"))
DEFAULT_REQUEST_TYPE = "b"

BORROW_STATUS = (
    ("borrowed", "Borrowed"),
    ("returned", "Returned"),
)

DEFAUL_BORROW_STATUS = "borrowed"
BORROW_STATUS_BORROW = 'borrowed'
BORROW_STATUS_RETURN = 'returned'
