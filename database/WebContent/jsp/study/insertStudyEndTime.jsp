<%@page import="database.co.kr.db.DBConn"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%
	/* 스터디 끝나는 시간 입력 */

	//한글 인코딩 부분
	request.setCharacterEncoding("utf-8");
	//커낵션 객체 생성
	DBConn conn = DBConn.getInstance();
	
	//필요한 파라미터
   	String id  = request.getParameter("id");
	
	
	// 작성 할 쿼리 
	String sql  = "UPDATE TBL_STD" 
				+" SET"  
				+" 	 STD_END = SYSDATE()" 
				+" WHERE "
				+"	 EMP_ID = '"+id+"'"
				+"	 AND STD_END = 'N''"
				+" ORDER  BY STD_SEQ DESC"; 
	
	//필요한 함수 호출(넘기는 매개변수 끝에 sql 넣기!!!)
	int result = conn.insertStudyEndTime(id,sql);
	
	//출력
	out.println(result);
	
	
%>
