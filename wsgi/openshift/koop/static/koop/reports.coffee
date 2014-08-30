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
    plugins: ['wholerow',]
  )

$(document).ready(document_loaded)