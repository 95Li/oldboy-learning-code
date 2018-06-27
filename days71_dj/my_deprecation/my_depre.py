from django.utils.deprecation import MiddlewareMixin


class MD1(MiddlewareMixin):
    yes_list = ['/login/']
    no_list = ['/home/']

    def process_request(self, request):
        from django.shortcuts import HttpResponse, render, redirect
        print('MD1 里的 process_request')

        url_next = request.path_info
        print(url_next)
        session = request.session.get('login')
        print(session)
        print(self.yes_list)
        if url_next in self.yes_list or session:
            return
        if url_next in self.no_list:
            return redirect('/login/')
        else:
            return redirect('/login/?next={}'.format(url_next))
