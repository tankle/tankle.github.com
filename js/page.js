(function(){
	/** 2015-05-29 
	 *  gaojun.zhou
	 * 设置分页组件和数据
	 * pageBarId 分页工具栏ID
	 * showDataId 展示数据的列表父容器ID
	 * tmplId jQuery模板ID
	 * data 所有数据集合
	 * pageSize 每页显示数据条数
	 * displaySize 最多可显示的分页主体页数
	 * entriesSize 边缘数
	 */
	function setDataAndPageBar(pageBarId,showDataId,tmplId,data,pageSize,displaySize,entriesSize){
		//这是一个非常简单的demo实例，让列表元素分页显示
		//回调函数的作用是显示对应分页的列表项内容
		//回调函数在用户每次点击分页链接的时候执行
		//参数page_index{int整型}表示当前的索引页
		var initPagination = function() {
			var num_entries = data.length;
			// 创建分页
			$(pageBarId).pagination(num_entries, {
				num_edge_entries: entriesSize?entriesSize:1, //边缘页数
				num_display_entries: displaySize?displaySize:8, //主体页数
				callback: pageselectCallback,
				items_per_page:pageSize 
			});
		 }();
		 //获取第N页的数据
		function getNumPageData(data1,pageSize1,page_index1){
			var d2 = [];
			var totalPage = data1.length % pageSize1 ==0 ? data1.length / pageSize1: parseInt(data1.length / pageSize1)+1;
			//alert();
			if(page_index1<totalPage-1){
				for(var i = pageSize1*page_index1;i<(pageSize1*page_index1)+pageSize1;i++){
					d2.push(data1[i]);
				}
			}else{
				for(var i = pageSize1*page_index1;i<data1.length;i++){
					d2.push(data1[i]);
				}
			}
			return d2;
		}
		function pageselectCallback(page_index, jq){			
			$(showDataId).empty(); //清空数据
			$(tmplId).tmpl(getNumPageData(data,pageSize,page_index)).appendTo(showDataId);
			return false;
		}
	
	}
	window.setDataAndPageBar  = setDataAndPageBar || {};
})();