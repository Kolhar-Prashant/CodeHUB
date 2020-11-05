def pageCount(n, p):
    def flip_pages_forward (dest_page,curr_page):
        if curr_page % 2 != 0:
            if dest_page - curr_page == 1:
                return 1
        if curr_page % 2 == 0:
            curr_page += 1
        Flip = 0
        while curr_page < dest_page:  # traversing in forward direction
            Flip += 1
            curr_page += 2
        return Flip

    def flip_page_backward (dest_page,last_page):
        curr_page = last_page
        if curr_page % 2 != 0:
            if curr_page - dest_page == 1:
                return 0
        if curr_page % 2 == 0:
            curr_page += 1
        if dest_page % 2 == 0:
            dest_page += 1
        Flip = 0
        while curr_page > dest_page:  # traversing in backward direction
            Flip += 1
            curr_page -= 2
        return Flip

    dest_page = p
    curr_page = 1
    last_page = n

    Flip_cnt_forward = flip_pages_forward (dest_page,curr_page)
    Flip_cnt_backward = flip_page_backward(dest_page, last_page)

    if Flip_cnt_forward < Flip_cnt_backward:
        return Flip_cnt_forward
    return Flip_cnt_backward