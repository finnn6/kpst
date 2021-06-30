<%@page import="database.co.kr.db.DBConn"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%
  	
	/*오늘 중에 가장 최근 공부한 시간과 과목 가져온다*/

	//한글 인코딩 부분
	request.setCharacterEncoding("utf-8");
	//커낵션 객체 생성
	DBConn conn = DBConn.getInstance();
	
	//필요한 파라미터
   	String id  = request.getParameter("id");
//    	id ="3ggk123";
	// 작성 할 쿼리 
	String sql  = "SELECT ts.STD_START , ts.STD_END "
			   		  +" ,tss.SUB_NAME "
		   		  +" FROM TBL_STD ts ,TBL_SUB_STD tss" 
		   		  +" WHERE ts.SUB_ID = tss.SUB_ID" 
		   		  +" AND ts.EMP_ID = '3ggk123'"
		   		  +" AND ts.STD_START > date_sub(now(), interval 1 day)" 
		   		  +" ORDER BY ts.STD_SEQ DESC"
		   		  +" LIMIT 0,1";
	              
	//필요한 함수 호출(넘기는 매개변수 끝에 sql 넣기!!!)
	String result = conn.getRecentStudyTime(id,sql);
	
	//출력
	out.println(result);
	
	
%>
