<%@page import="database.co.kr.db.DBConn"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%
  	
	/*검색어 순위 출력*/
	
	//한글 인코딩 부분
	request.setCharacterEncoding("utf-8");
	//커낵션 객체 생성
	DBConn conn = DBConn.getInstance();
	
	//필요한 파라미터
   	//String keyword  = request.getParameter("keyword");
	
	// 작성 할 쿼리 
	String sql = "SELECT"
				+"			@rownum:=@rownum+1 AS \"RANKING\""
				+"			,SEARCH_WORD"
				+"			,SEARCH_CNT "
				+"		FROM "
				+"			TBL_VOICE_REC tvr" 
				+"		WHERE (SELECT @rownum:=0)=0"
				+" 	    ORDER BY SEARCH_CNT DESC";
	
	//필요한 함수 호출(넘기는 매개변수 끝에 sql 넣기!!!)
	String result = conn.getKeywordRank(sql);
	
	//출력
	out.println(result);
	
	
%>
