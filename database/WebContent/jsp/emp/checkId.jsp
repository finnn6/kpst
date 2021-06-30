<%@page import="database.co.kr.db.DBConn"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%
  	

//한글 인코딩 부분
	request.setCharacterEncoding("utf-8");

	//커낵션 객체 생성
	DBConn conn = DBConn.getInstance();
	
	//필요한 파라미터

	
	String id = request.getParameter("id");
	id = "sys";
	// 작성 할 쿼리 
	
	
	String sql  = "SELECT * FROM TBL_EMP te WHERE EMP_ID = '"+id+"'";

	
	//필요한 함수 호출(넘기는 매개변수 끝에 sql 넣기!!!)
	String result = conn.checkId(sql);
	
	//출력
	out.println(result);
	
%>

	