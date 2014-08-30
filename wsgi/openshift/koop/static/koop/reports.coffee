NODETYPE_FOLDER = 'folder'
NODETYPE_REPORT = 'report'

document_loaded = () ->
  $('#folderFormsContainer').hide()
  $('#reportFormsContainer').hide()
  setup_tree()
  enable_tabs()

enable_tabs = () ->
  $('#folderTabList a').click((e) =>
    e.preventDefault()
    $(this).tab('show')
  )

node_selected = (e, data) ->
  if data.node.type == NODETYPE_FOLDER
    update_folder_form(data.node)
  else if data.node.type == NODETYPE_REPORT
    update_report_form(data.node)

update_report_form = (reportNode) ->
  $('#folderFormsContainer').hide()
  $('#reportFormsContainer').show()

update_folder_form = (folderNode) ->
  $('#reportFormsContainer').hide()
  $('#folderFormsContainer').show()
  $('#folderName').text(folderNode.text)

setup_tree = () ->
  treeContainer = $('#reportsTree')
  $(treeContainer).jstree(
    core:
      themes:
        variant: 'large'
      data:
        url: '/api/tree'
      multiple: false
    types:
      folder:
        icon: 'glyphicon glyphicon-folder-open'
        valid_children: [NODETYPE_FOLDER, NODETYPE_REPORT]
      report:
        icon: 'glyphicon glyphicon-file'
        valid_children: []
    plugins: ['wholerow',
              'state',
              'types',
    ]
  )
  $(treeContainer).on('select_node.jstree', node_selected)

$(document).ready(document_loaded)