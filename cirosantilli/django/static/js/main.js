//<datatable

    //var asInitVals = new Array();
    var datatable_filter_target_table_attr = 'target_table'
    var datatable_filter_target_col_attr = 'target_column'

    var datatable_global_prefix = 'datatable_global_'
    var datatable_col_prefix = 'datatable_col_'

    var datatable_global_filter_class = datatable_global_prefix + 'filter'
    var datatable_global_regex_class = datatable_global_prefix + 'regex'
    var datatable_global_smart_class = datatable_global_prefix + 'smart'

    var datatable_col_filter_class = datatable_col_prefix + 'filter'
    var datatable_col_regex_class = datatable_col_prefix + 'regex'
    var datatable_col_smart_class = datatable_col_prefix + 'smart'


    //filters table with given table_id globally
    function fnFilterGlobal ( table_id )
    {
        $('#'+table_id).dataTable().fnFilter(

            $('body').find(
              '.'+datatable_global_filter_class
            ).filter(
              '['+datatable_filter_target_table_attr+'='+table_id+']' 
            ).val(),

            null,

            $('body').find(
              '.'+datatable_global_regex_class
            ).filter(
              '['+datatable_filter_target_table_attr+'='+table_id+']' 
            )[0].checked,

            $('body').find(
              '.'+datatable_global_smart_class
            ).filter(
              '['+datatable_filter_target_table_attr+'='+table_id+']' 
            )[0].checked

        );
    }
    
    //filters table with given table_id globally according to column i
    function fnFilterColumn ( table_id, i )
    {
        $('#'+table_id).dataTable().fnFilter(

            $('body').find(
              '.'+datatable_global_filter_class
            ).filter(
              '['+datatable_filter_target_table_attr+'='+table_id+']' 
            ).filter(
              '['+datatable_filter_target_col_attr+'='+i+']' 
            ).val(),

            i,

            $('body').find(
              '.'+datatable_global_regex_class
            ).filter(
              '['+datatable_filter_target_table_attr+'='+table_id+']' 
            ).filter(
              '['+datatable_filter_target_col_attr+'='+i+']' 
            )[0].checked,

            $('body').find(
              '.'+datatable_global_smart_class
            ).filter(
              '['+datatable_filter_target_table_attr+'='+table_id+']' 
            ).filter(
              '['+datatable_filter_target_col_attr+'='+i+']' 
            )[0].checked
        );
    }

//>datatable

//<autocumplete

  var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
  ];

  function split( val ) {
      return val.split( /,\s*/ );
  }
  function extractLast( term ) {
      return split( term ).pop();
  }

//>autocumplete
 
$(document).ready(function() 
    { 
        //<dataTable
 
            //overkill table pagination, sort and search

            var oTable = $('.datatable').dataTable( {
                    "oLanguage": {
                        "sSearch": "search all: ",
                        "sLengthMenu": "entries per page: _MENU_",
                        "sZeroRecords": "no entries",
                        "sInfo": "_START_ to _END_ of _TOTAL_",
                        "sInfoEmpty": "0 to 0 of 0",
                        //"sInfoFiltered": "(filtered from _MAX_ total records)"
                    },
                    "aoColumnDefs": [
                      { "bSortable": false, "aTargets": [ 'nosort' ] },
                    ],
                    //"sDom": 'rt<"bottom"iflp<"clear">>', //order of elements
                    "sDom": '<"top"><"clear">rt', //order of elements
                    "iDisplayLength": -1,
                    "aLengthMenu": [[10, 25, 50, 100, 1000, -1], [10, 25, 50, 100, 1000, "all" ]],
                    //firefox http://www.datatables.net/release-datatables/examples/basic_init/dom.html
                } );


            //tfoot input filtering
                //oTable.find("tfoot input").keyup( function () {
                    //oTable.fnFilter( this.value, $("tfoot td").index($(this).parent()) );
                //} );

                //oTable.find("tfoot input").each( function (i) {
                    //asInitVals[i] = this.value;
                //} );
                
                //oTable.find("tfoot input").focus( function () {
                    //if ( this.className == "search_init" )
                    //{
                        //this.className = "";
                        //this.value = "";
                    //}
                //} );
                
                //oTable.find("tfoot input").blur( function (i) {
                    //if ( this.value == "" )
                    //{
                        //this.className = "search_init";
                        //this.value = asInitVals[$("tfoot input").index(this)];
                    //}
                //} );

            //separate input filtering
                //assumes that each filter, regex and smart is in the same column
                
                var datatable_global_filter_class = datatable_global_prefix + 'filter';
                var datatable_global_regex_class = datatable_global_prefix + 'regex';
                var datatable_global_smart_class = datatable_global_prefix + 'smart';

                var datatable_col_filter_class = datatable_col_prefix + 'filter';
                var datatable_col_regex_class = datatable_col_prefix + 'regex';
                var datatable_col_smart_class = datatable_col_prefix + 'smart';

                $("input." + datatable_global_filter_class ).keyup( function() { fnFilterGlobal( $(this).attr(datatable_filter_target_table_attr) ); } );
                $("input." + datatable_global_regex_class ).click( function() { fnFilterGlobal( $(this).attr(datatable_filter_target_table_attr) ); } );
                $("input." + datatable_global_smart_class ).click( function() { fnFilterGlobal( $(this).attr(datatable_filter_target_table_attr) ); } );
                
                $("input." + datatable_col_filter_class ).keyup( function() { fnFilterColumn( $(this).attr(datatable_filter_target_table_attr), $(this).attr(datatable_filter_target_col_attr) ); } );
                $("input." + datatable_col_regex_class ).click( function() { fnFilterColumn( $(this).attr(datatable_filter_target_table_attr), $(this).attr(datatable_filter_target_col_attr) ); } );
                $("input." + datatable_col_smart_class ).click( function() { fnFilterColumn( $(this).attr(datatable_filter_target_table_attr), $(this).attr(datatable_filter_target_col_attr) ); } );

        //>dataTable

        //<autocumplete
        $( ".jquery-ui-autocomplete" )
            // don't navigate away from the field on tab when selecting an item
            .bind( "keydown", function( event ) {
                if ( event.keyCode === $.ui.keyCode.TAB &&
                        $( this ).data( "autocomplete" ).menu.active ) {
                    event.preventDefault();
                }
            })
            .autocomplete({
                minLength: 0,
                source: function( request, response ) {
                    // delegate back to autocomplete, but extract the last term
                    response( $.ui.autocomplete.filter(
                        availableTags, extractLast( request.term ) ) );
                },
                focus: function() {
                    // prevent value inserted on focus
                    return false;
                },
                select: function( event, ui ) {
                    var terms = split( this.value );
                    // remove the current input
                    terms.pop();
                    // add the selected item
                    terms.push( ui.item.value );
                    // add placeholder to get the comma-and-space at the end
                    terms.push( "" );
                    this.value = terms.join( "\n" );
                    return false;
                }
            });

          //$( ".jquery-ui-autocomplete" ).autocomplete({
                      //source: availableTags
                  //});

        //<autocumplete

 
        //<master checkbox
            //a checkbox that controls multiple checkboxes
            //give it class master-checkbox and an id
            //and for the checkbox it controls give them slave-of attribute equal to the mater's id
            //  each slave can have multiple masters, space separated
            $('.master-checkbox').click(function() {
                $('body').find('[slave-of~="'+$(this).attr('id')+'"]').attr('checked', this.checked );
            });     
        //>master checkbox
    } 
); 
