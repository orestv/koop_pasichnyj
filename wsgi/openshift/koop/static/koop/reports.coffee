NODETYPE_FOLDER = 'folder'
NODETYPE_REPORT = 'report'

document_loaded = () ->
  $('#folderFormsContainer').hide()
  $('#reportFormsContainer').hide()
  $('#uploadProgressOuter').hide()
  setup_tree()
  enable_tabs()
  init_upload_form()

init_upload_form = () ->
  $('#fileUploadForm').ajaxForm(
    beforeSubmit: upload_before_submit
    resetForm: true
    error: () -> alert 'An error has occurred!'
    success: upload_success
    uploadProgress: upload_progress
  )

upload_before_submit = () ->
  $('#fileUploadForm input[type="submit"]').button('loading')
  set_upload_progress_percentage(0)
  $('#uploadProgressOuter').show()

upload_success = (responseText, statusText, xhr, form) ->
  $('#fileUploadForm input[type="submit"]').button('reset')
  $('#uploadProgressOuter').hide()
  $('#uploadSuccessAlert').show()
  setTimeout((() -> $('#uploadSuccessAlert').fadeOut()), 1500)
  $('#reportsTree').jstree('refresh')

upload_progress = (event, position, total, percentComplete) ->
  console.log percentComplete
  set_upload_progress_percentage(percentComplete)

set_upload_progress_percentage = (percentage) ->
  $('#uploadProgressInner').css('width', "#{percentage}%")
  $('#uploadProgressInner').html("#{percentage}%")

enable_tabs = () ->
#  $('#folderTabList a').click((e) =>
#    e.preventDefault()
#    $(this).tab('show')
#  )

node_selected = (e, data) ->
  if data.node.type == NODETYPE_FOLDER
    folder_node_selected(data.node)
  else if data.node.type == NODETYPE_REPORT
    report_node_selected(data.node)

report_node_selected = (reportNode) ->
  $('#folderFormsContainer').hide()
  $('#reportFormsContainer').show()
  $('#folderButtonsFieldset').attr('disabled', 'disabled')

folder_node_selected = (folderNode) ->
  $('#reportFormsContainer').hide()
  $('#folderFormsContainer').show()
  $('#folderName').text(folderNode.text)
  $('#fileUploadFolderId').val(folderNode.id)
  if folderNode.parent == '#'
    $('#btnDeleteFolder').attr('disabled', 'disabled')
  else
    $('#btnDeleteFolder').removeAttr('disabled')
  $('#folderButtonsFieldset').removeAttr('disabled')

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