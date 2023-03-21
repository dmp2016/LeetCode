class BrowserHistory:

    def __init__(self, homepage: str):
        self.url_list = [homepage]
        self.cur_ind = 0

    def visit(self, url: str) -> None:
        self.url_list = self.url_list[:self.cur_ind + 1] + [url]
        self.cur_ind += 1

    def back(self, steps: int) -> str:
        self.cur_ind -= steps
        if self.cur_ind < 0:
            self.cur_ind = 0
        return self.url_list[self.cur_ind]

    def forward(self, steps: int) -> str:
        self.cur_ind += steps
        if self.cur_ind >= len(self.url_list):
            self.cur_ind = len(self.url_list) - 1
        return self.url_list[self.cur_ind]
