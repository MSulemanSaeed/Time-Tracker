from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "pageSize"
    max_page_size = 50
        

    def get_paginated_response(self, data):

        return Response(
            {
                # 'next': self.get_next_link(),
                # 'previous': self.get_previous_link(),
                "results": data,
                "pagination": {
                    "total": self.page.paginator.count,
                    "current": self.page.number,
                    "pageSize": self.page_size,
                },
            }
        )