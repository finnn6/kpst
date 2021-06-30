package database.co.kr.db;

import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;


public class jsonTest {
	public static void main(String[] args) {
		JSONObject jsonMain = new JSONObject(); 
		JSONArray jArray = new JSONArray(); 
		JSONObject jObject = new JSONObject(); 
		
		
		type ty = new type();
		List<type> test2  = new ArrayList<type>();
		test2.add(ty);
		
		type[] test3 = {ty};
		jObject.put("testList", ty.toString());
		System.out.println(jObject);
		
	}
	public static class type {
		String ty1 = "test1";
		String ty2 = "test2";
		String ty3 = "test3";
		@Override
		public String toString() {
			return "type [ty1=" + ty1 + ", ty2=" + ty2 + ", ty3=" + ty3 + "]";
		}
		
	}
}
