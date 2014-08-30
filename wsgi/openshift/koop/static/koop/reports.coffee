document_loaded = () ->
  setup_tree()

setup_tree = () ->
  $('#reportsTree').jstree(
    core:
      themes:
        variant: 'large'
      data:
        url: '/api/tree'
      multiple: false
    types:
      folder:
        icon: 'glyphicon glyphicon-folder-open'
        valid_children: ['folder', 'report']
      report:
        icon: 'glyphicon glyphicon-file'
        valid_children: []
    plugins: ['wholerow',
              'state',
              'types',
    ]
  )

$(document).ready(document_loaded)