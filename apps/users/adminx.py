from apps.users.models import UserProfile, EmailVerifyRecord, Banner
import xadmin
from xadmin import views



class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """
    设置网站页头页尾
    """
    site_title = "在线教育后台管理系统"
    site_footer = "Powered By 1906C - 2020"
    menu_style = "accordion" # 设置菜单折叠


class UserProfileAdmin(object):
    list_display = ["username", "gender", "mobile", "address" ]
    search_fields = ["username", "gender", "mobile", "address"]
    list_filter = ["username", "gender", "mobile", "address"]
    model_icon = 'fa fa-user'
    style_fields = {"address": "ueditor"}
    ordering = ["-date_joined"]   # 排序 、 date_joined前加-号为最新时间排序
    readonly_fields = ["nick_name"]  # 只读字段，不能编辑
    exclude = ["gender"]  # 不显示字段
    list_editable = ["mobile"]
    refresh_times = [3, 5] # 每隔3或5秒刷新一次


class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
