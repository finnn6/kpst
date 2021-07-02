package database.co.kr.db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

public  class DBConn {
	
	
	/*싱글톤*/
	private static DBConn instance = new DBConn();
	public static DBConn getInstance() {
		return instance;
	}
	public DBConn() {}

	/*자원 관련*/
	/**
	 * 연동 함수	
	 * @author minsoo
	 *
	 */
	public static class Resource{
		final String driver = "org.mariadb.jdbc.Driver";
		final String DB_IP = "localhost";
		final String DB_PORT = "3306";
		final String DB_NAME = "study_db";
		final String DB_URL = "jdbc:mariadb://" + DB_IP + ":" + DB_PORT + "/" + DB_NAME;
	}
	/**
	 * 자원 반납함수
	 * @param rs
	 * @param pstmt
	 * @param conn
	 * @throws SQLException
	 */
	public static void closeResource(ResultSet rs, PreparedStatement pstmt, Connection conn) throws SQLException {
		if (rs != null) rs.close();
		if (pstmt != null) pstmt.close();
		if (conn != null && !conn.isClosed()) conn.close();
	}
	/**
	 * 자원 연결 메서드
	 * @param conn
	 * @param pstmt
	 * @param rs
	 */
	private static Connection makeConnection() {
		//연결 객체 생성
		Resource connInfo = new Resource();

		//자원 생성
		Connection conn = null;

		try {
			Class.forName(connInfo.driver);
			conn = DriverManager.getConnection(connInfo.DB_URL, "study_db", "1111");
			if (conn != null) {
				System.out.println("DB 접속 성공");
			}

		} catch (ClassNotFoundException e) {
			System.out.println("드라이버 로드 실패");
			e.printStackTrace();
		} catch (SQLException e) {
			System.out.println("DB 접속 실패");
			e.printStackTrace();
		}
		return conn;
	}
	public static int testDBMethod(String id , String pw,String sql){	
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();


		//필요한 변수,객체 선언
		int ans = 0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();

			//값을 입력
			while (rs.next()) {
				ans = rs.getInt(1);
				System.out.println("쿼리 값"+ans);
			}

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return ans;
	}

	/*공부 관련*/
	/**
	 *오늘 중에 가장 최근 공부한 시간과 과목 가져온다
	 * @param id
	 * @param sql
	 * @return
	 */
	public static String getRecentStudyTime(String id ,String sql) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		Date date = new Date();
		SimpleDateFormat transFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

		String result ="";

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();

			//값을 입력
			while (rs.next()) {
				JSONObject jObject = new JSONObject();
				jObject.put("STD_START", rs.getString(1));
				jObject.put("STD_END", rs.getString(1));
				jObject.put("SUB_NAME", rs.getString(2));

				System.out.println("쿼리 값\n"+sql);
				System.out.println("데이터\n"+jObject);
				result = jObject.toString();
			}

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	}
	/**
	 * 오늘 공부한 시간 가져오기
	 * @param id
	 * @param sql
	 * @return
	 */
	@SuppressWarnings("unchecked")
	public static String getTodayStudyTime(String id ,String sql) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		//		Date date = new Date();
		//		SimpleDateFormat transFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

		JSONArray jArray = new JSONArray();
		String result ="";

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();

			//값을 입력
			while (rs.next()) {
				JSONObject jObject = new JSONObject();
				jObject.put("STD_SEQ", rs.getObject("STD_SEQ"));
				jObject.put("STD_START", rs.getObject("STD_START"));
				jObject.put("STD_END", rs.getObject("STD_END"));
				jObject.put("EMP_ID", rs.getObject("EMP_ID"));
				jObject.put("SUB_ID", rs.getObject("SUB_ID"));	
				jObject.put("SUB_NAME", rs.getObject("SUB_NAME"));
				jArray.add(jObject);
			}
			result = jArray.toJSONString();
			System.out.println("쿼리 값\n"+sql);
			System.out.println("데이터\n"+result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	}
	/**
	 * 스터디 끝나는 시간 입력
	 * @param id
	 * @param sql
	 * @return
	 */
	public static int insertStudyEndTime(String id, String sql ) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		int result =0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			result = 1;
			rs = pstmt.executeQuery();
			System.out.println("쿼리 값\n"+sql);
			System.out.println("데이터\n"+result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	}
	/**
	 * 스터디 시작시간 입력
	 * @param sql
	 * @return
	 */
	public  static int insertStudyStartTime(String sql) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		int result =0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			result = 1;
			rs = pstmt.executeQuery();
			System.out.println("쿼리 값\n"+sql);
			System.out.println("데이터\n"+result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	}
	/**
	 * 모든 공부 시간 출력
	 * @param sql
	 * @return
	 */
	public static String selectAllStudyTime(String sql) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		//		Date date = new Date();
		//		SimpleDateFormat transFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

		JSONArray jArray = new JSONArray();
		String result ="";

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();

			//값을 입력
			while (rs.next()) {
				JSONObject jObject = new JSONObject();
				jObject.put("STD_SEQ", rs.getObject("STD_SEQ"));
				jObject.put("STD_START", rs.getObject("STD_START"));
				jObject.put("STD_END", rs.getObject("STD_END"));
				jObject.put("EMP_ID", rs.getObject("EMP_ID"));
				jObject.put("SUB_NAME", rs.getObject("SUB_NAME"));		                               
				jArray.add(jObject);
			}
			result = jArray.toJSONString();
			System.out.println("쿼리 값\n"+sql);
			System.out.println("데이터\n"+result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	}
	/**
	 * 현재 공부 상태 알림
	 * @param sql
	 * @return
	 */
	public static int studyStatus(String sql) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		//				Date date = new Date();
		//				SimpleDateFormat transFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		JSONObject jObject = new JSONObject();
		JSONArray jArray = new JSONArray();
		int result =0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();
			while (rs.next()) {

				result = rs.getInt(1);
			}
			System.out.println("쿼리 값\n"+sql);
			System.out.println("데이터\n"+result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	}

	/*검색어 관련*/
	/**
	 * 검색어 순위로 출력	
	 * @param sql
	 * @return
	 */
	public static String getKeywordRank(String sql) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		JSONArray jArray = new JSONArray();
		String result ="";

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();
			int i=1;
			//값을 입력
			while (rs.next()) {
				JSONObject jObject = new JSONObject();
				jObject.put("RANKING", i++);
				jObject.put("SEARCH_WORD", rs.getObject("SEARCH_WORD"));
				jObject.put("SEARCH_CNT", rs.getObject("SEARCH_CNT"));
				jArray.add(jObject);
			}
			result = jArray.toJSONString();
			System.out.println("쿼리 값\n"+sql);
			System.out.println("데이터\n"+result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	}
	/**
	 * 키워드 입력
	 * @param sql
	 * @return
	 */
	public static int insertKeyword(String sql) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		JSONArray jArray = new JSONArray();
		int result =0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();
			result = 1;

			System.out.println("쿼리 값\n"+sql);
			System.out.println("데이터\n"+result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	};
	/**
	 * 검색어 cnt 증가
	 * @param sql
	 * @return
	 */
	public static int increaseKeywordCnt(String sql) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		JSONArray jArray = new JSONArray();
		int result =0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();
			result = 1;

			System.out.println("쿼리 값\n"+sql);
			System.out.println("데이터\n"+result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	}
	/**
	 * 검색어가 있으면 1 반환
	 * @param sql
	 * @return
	 */
	public static int searchKeyword(String sql) {
		//자원 선언
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Connection conn = makeConnection();

		//필요한 변수,객체 선언 (date 필요하면 쓰세욜)
		int result =0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();
			result = 1;

			System.out.println("쿼리 값\n"+sql);
			System.out.println("데이터\n"+result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return result ;
	}

	/*회원생성*/
	/** 
	 * 로그인 
	 * @param id
	 * @param pw
	 * @param sql
	 * @return
	 */
	public static int logIn(String sql){	
		//자원 선언
		Connection conn = makeConnection();
		PreparedStatement pstmt = null;
		ResultSet rs = null;


		//필요한 변수,객체 선언
		int ans = 0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();

			//값을 입력
			while (rs.next()) {
				ans = rs.getInt(1);
				System.out.println("쿼리 값"+ans);
			}


		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return ans;
	}
	/**
	 * 회원 생성
	 * @param id
	 * @param pw
	 * @param name
	 * @param bir
	 * @param ph
	 * @param rec
	 * @param sql
	 * @return
	 */
	public static int createEmp(String id , String pw,String name,String bir,String ph,String rec,String sql){	
		//자원 선언
		Connection conn = makeConnection();
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		//연동 테스트



		//필요한 변수,객체 선언
		int ans = 0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();
			ans = 1;
			//값을 입력
			while (rs.next()) {
				ans = rs.getInt(1);
				System.out.println("쿼리 값"+ans);
			}


		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴
		return ans;
	}
	/**
	 * 회원 정보 수정
	 * @param pw
	 * @param name
	 * @param ph
	 * @param id
	 * @param sql
	 * @return
	 */
	public static int updateEmp(String sql) {
		//자원 선언
		Connection conn = makeConnection();
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		//연동 테스트



		//필요한 변수,객체 선언
		int ans = 0;

		try {
			
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();
			ans = 1;
			//값을 입력
			while (rs.next()) {
				ans = rs.getInt(1);
				System.out.println("쿼리 값"+ans);
			}


		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴

		return ans;
	}
	/**
	 * 회원 검색
	 * @param id
	 * @param sql
	 * @return
	 */
	public static String checkId(String sql) {
		Connection conn = makeConnection();
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		//연동 테스트

		//필요한 변수,객체 선언
		String result = "";

		JSONArray jArray = new JSONArray();
		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();

			//값을 입력
			while (rs.next()) {
				jArray.add(rs.getString("EMP_ID"));
				jArray.add(rs.getString("PWD"));
				jArray.add(rs.getString("NAME"));	
				jArray.add(rs.getString("BIR"));
				jArray.add(rs.getString("PH"));
				jArray.add(rs.getString("INTROD_ID"));
			}
			result = jArray.toJSONString();
			System.out.println(result);

		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴

		return result;
	}
	/**
	 * 회원 삭제
	 * @param sql
	 * @return
	 */
	public static int deleteEmp(String sql) {

		Connection conn = makeConnection();
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		//연동 테스트


		//필요한 변수,객체 선언
		int ans = 0;

		try {
			//쿼리 날린값
			pstmt = conn.prepareStatement(sql);
			//값 받아오기
			rs = pstmt.executeQuery();
			ans = 1;
			//값을 입력
			while (rs.next()) {
				ans = rs.getInt(1);
				System.out.println("쿼리 값"+ans);
			}


		} catch (SQLException e) {
			System.out.println("error: " + e);
		} finally {
			try {
				closeResource(rs,pstmt,conn); 
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		//반환 값이 있다면 리턴

		return ans;
	}
}