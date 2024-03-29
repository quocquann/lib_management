BOOK_COPY_STATUS = ((0, "Available"), (1, "Borrowed"))

REQUEST_STATUS = (("pending", "pending"), ('rejected', "rejected"), ("approved", "approved"))
DEFAULT_REQUEST_STATUS = "pending"

REQUEST_TYPE = (("borrow", "Borrow"), ("renew", "Renew"))
DEFAULT_REQUEST_TYPE = "b"

BORROW_STATUS = (
    ("borrowed", "Borrowed"),
    ("returned", "Returned"),
)

DEFAUL_BORROW_STATUS = "borrowed"
