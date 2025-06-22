# api/mypaginations.py
from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'  # make sure this field exists in Student model
    cursor_query_param = 'cu'  # optional: your custom query param
