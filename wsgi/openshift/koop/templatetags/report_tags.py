from django import template

register = template.Library()


@register.inclusion_tag('koop/reports_folder.html')
def folder_tag(folder):
    children = folder.children.all()
    return {'folder': folder,
            'children': children,
           }