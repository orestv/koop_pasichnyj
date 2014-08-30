// Generated by CoffeeScript 1.4.0
(function() {
  var NODETYPE_FOLDER, NODETYPE_REPORT, document_loaded, enable_tabs, init_upload_form, node_selected, set_upload_progress_percentage, setup_tree, update_folder_form, update_report_form, upload_before_submit, upload_progress, upload_success;

  NODETYPE_FOLDER = 'folder';

  NODETYPE_REPORT = 'report';

  document_loaded = function() {
    $('#folderFormsContainer').hide();
    $('#reportFormsContainer').hide();
    $('#uploadProgressOuter').hide();
    setup_tree();
    enable_tabs();
    return init_upload_form();
  };

  init_upload_form = function() {
    return $('#fileUploadForm').ajaxForm({
      beforeSubmit: upload_before_submit,
      resetForm: true,
      error: function() {
        return alert('An error has occurred!');
      },
      success: upload_success,
      uploadProgress: upload_progress
    });
  };

  upload_before_submit = function() {
    $('#fileUploadForm input[type="submit"]').button('loading');
    set_upload_progress_percentage(0);
    return $('#uploadProgressOuter').show();
  };

  upload_success = function(responseText, statusText, xhr, form) {
    $('#fileUploadForm input[type="submit"]').button('reset');
    $('#uploadProgressOuter').hide();
    $('#uploadSuccessAlert').show();
    setTimeout((function() {
      return $('#uploadSuccessAlert').fadeOut();
    }), 1500);
    return $('#reportsTree').jstree('refresh');
  };

  upload_progress = function(event, position, total, percentComplete) {
    console.log(percentComplete);
    return set_upload_progress_percentage(percentComplete);
  };

  set_upload_progress_percentage = function(percentage) {
    $('#uploadProgressInner').css('width', "" + percentage + "%");
    return $('#uploadProgressInner').html("" + percentage + "%");
  };

  enable_tabs = function() {
    var _this = this;
    return $('#folderTabList a').click(function(e) {
      e.preventDefault();
      return $(_this).tab('show');
    });
  };

  node_selected = function(e, data) {
    if (data.node.type === NODETYPE_FOLDER) {
      return update_folder_form(data.node);
    } else if (data.node.type === NODETYPE_REPORT) {
      return update_report_form(data.node);
    }
  };

  update_report_form = function(reportNode) {
    $('#folderFormsContainer').hide();
    return $('#reportFormsContainer').show();
  };

  update_folder_form = function(folderNode) {
    $('#reportFormsContainer').hide();
    $('#folderFormsContainer').show();
    $('#folderName').text(folderNode.text);
    return $('#fileUploadFolderId').val(folderNode.id);
  };

  setup_tree = function() {
    var treeContainer;
    treeContainer = $('#reportsTree');
    $(treeContainer).jstree({
      core: {
        themes: {
          variant: 'large'
        },
        data: {
          url: '/api/tree'
        },
        multiple: false
      },
      types: {
        folder: {
          icon: 'glyphicon glyphicon-folder-open',
          valid_children: [NODETYPE_FOLDER, NODETYPE_REPORT]
        },
        report: {
          icon: 'glyphicon glyphicon-file',
          valid_children: []
        }
      },
      plugins: ['wholerow', 'state', 'types']
    });
    return $(treeContainer).on('select_node.jstree', node_selected);
  };

  $(document).ready(document_loaded);

}).call(this);
