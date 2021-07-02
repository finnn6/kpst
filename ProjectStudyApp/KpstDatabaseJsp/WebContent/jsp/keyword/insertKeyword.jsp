<%@page import="database.co.kr.db.DBConn"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%
  	
	/* 검색어 입력 */
	
	//한글 인코딩 부분
	request.setCharacterEncoding("utf-8");
	//커낵션 객체 생성
	DBConn conn = DBConn.getInstance();
	
	//필요한 파라미터
	String keyword = request.getParameter("keyword");
// 	keyword = "json";
	// 작성 할 쿼리 
	String sql  = "INSERT into TBL_VOICE_REC values (nextval(SEQ_TBL_VOICE_REC),'"+keyword+"',1)";
	
	//필요한 함수 호출(넘기는 매개변수 끝에 sql 넣기!!!)
	int result = conn.insertStudyStartTime(sql);
	
	//출력
	out.println(result);
	
	
%>
