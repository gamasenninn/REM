var mixinHeader={

  data:{
       //------Config area-----
       perPage: 10,
       currentPage: 1,
       listFields: [
           {  key: 'h_id',        label: 'ID',      width: '5%', sortable: true },
           {  key: 'category',    label: '書類種別', width: '10%', sortable: true },
           {  key: 'client_name', label: '顧客名',   width: '30%', sortable: true },
           {  key: 'client_class',label: '区分',     width: '5%', sortable: true  },
           {  key: 'apply_date',  label: '摘要日付', width: '10%', sortable: true },
           {  key: 'person',      label: '担当',   width: '8%', sortable: true },
           {  key: 'doc_descript',label: '摘要欄',   width: '', sortable: true  },
           {  key: 'control',     label: '操作',     width: '10%', class: 'text-center'},
       ],
       editFields:[
           {  key: 'h_id',        label: 'ID',      type: null,
                    pkey: true,   auto_increment: true
           },
           {  key: 'category',    label: '書類種別', type: 'select', selopt: 'category'},
           {  key: 'client_name', label: '顧客名',   type: 'text'},
           {  key: 'client_class',label: '区分(個人・法人)',     type: 'select', selopt: 'client_class'},
           {  key: 'apply_date',  label: '摘要日付', type: 'date' },
           {  key: 'person',      label: '弊社担当者',   type: 'select' , selopt: 'person'},
           {  key: 'doc_descript',label: '摘要欄',   type: 'textarea'},
       ],
       options:{
             category: [
                       { value: '見積書', text:'見積書'},
                       { value: '納品書', text:'納品書'},
                       { value: '請求書', text:'請求書'},
                 ],
             client_class: [
                       { value: '法人', text:'法人'},
                       { value: '個人', text:'個人'},
                 ],
             person: [
                       { value: '田中', text:'田中'},
                       { value: '佐藤', text:'佐藤'},
                       { value: '鈴木', text:'鈴木'},
                       { value: '小野', text:'小野'},
                       { value: '山田', text:'山田'},
                 ],
       },
       label:{
         title_header: '書類作成アプリ',
         add_data: 'データの追加',
         update_data: 'データの更新',
         delete_data: 'データの削除',
         cancel: 'キャンセル',
         confirm_delete: 'データを削除してよろしいですか',
       },
       apiEndPoint:{
         get:     '/remapi/doc_header',
         getByKey:'',
         post:    '/remapi/doc_header',
         put:     '/remapi/doc_header/h_id',
         delete:  '/remapi/doc_header/h_id',
       },
  }
};
