<%@page import="database.co.kr.db.DBConn"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%
	/*모든 공부시간을 출력해준다*/



	//한글 인코딩 부분
	request.setCharacterEncoding("utf-8");
	//커낵션 객체 생성
	DBConn conn = DBConn.getInstance();
	
	//필요한 파라미터
   	String id  = request.getParameter("id");
   	id ="3ggk123";
	// 작성 할 쿼리 
	String sql  = "SELECT STD_SEQ ,ts.STD_START ,ts.STD_END ,ts.EMP_ID,ts.SUB_ID,tss.SUB_NAME"
					+" FROM TBL_STD ts,TBL_SUB_STD tss " 
					+" WHERE  ts.SUB_ID = tss.SUB_ID "
					+" AND EMP_ID = '"+id+"'"
					+" AND STD_START > date_sub(now(), interval 1 day)" 
					+" ORDER BY STD_SEQ DESC";
				

	//필요한 함수 호출(넘기는 매개변수 끝에 sql 넣기!!!)
	String result = conn.getTodayStudyTime(id,sql);
	
	//출력
	out.println(result);
	
%>
