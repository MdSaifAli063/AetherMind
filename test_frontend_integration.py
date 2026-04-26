"""
Frontend & Backend Integration Test
Tests all endpoints that the frontend uses
"""
import json
import sys

def test_frontend_integration():
    """Test all frontend-backend interactions"""
    
    try:
        import app.app as flask_app
        app = flask_app.app
    except ImportError as e:
        print(f"[FAIL] Could not import Flask app: {e}")
        return False
    
    success_count = 0
    total_tests = 0
    
    with app.test_client() as client:
        print("=" * 70)
        print("FRONTEND & BACKEND INTEGRATION TEST")
        print("=" * 70)
        
        # Test 1: Health Check
        print("\n[1] Health Check")
        total_tests += 1
        try:
            resp = client.get('/health')
            if resp.status_code == 200:
                print("    [OK] /health -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /health -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 2: Dashboard
        print("\n[2] Dashboard Page")
        total_tests += 1
        try:
            resp = client.get('/dashboard')
            if resp.status_code == 200 and 'OpenEnv' in resp.data.decode():
                print("    [OK] /dashboard -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /dashboard -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 3: Run Episode
        print("\n[3] Run Episode API")
        total_tests += 1
        try:
            resp = client.post('/api/run-episode')
            data = resp.get_json()
            if resp.status_code == 200 and 'reward' in data:
                print(f"    [OK] /api/run-episode -> Reward: {data['reward']}")
                success_count += 1
            else:
                print(f"    [FAIL] /api/run-episode -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 4: Get Episodes
        print("\n[4] Get Episodes API")
        total_tests += 1
        try:
            resp = client.get('/api/episodes')
            data = resp.get_json()
            if resp.status_code == 200 and 'episodes' in data:
                print(f"    [OK] /api/episodes -> {data['total']} episodes")
                success_count += 1
            else:
                print(f"    [FAIL] /api/episodes -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 5: Latest Episode
        print("\n[5] Latest Episode API")
        total_tests += 1
        try:
            resp = client.get('/api/episode/latest')
            data = resp.get_json()
            if resp.status_code == 200:
                print(f"    [OK] /api/episode/latest -> {data.get('persona',{}).get('name', 'N/A')}")
                success_count += 1
            else:
                print(f"    [FAIL] /api/episode/latest -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 6: Resolve Endpoint
        print("\n[6] Resolve Conflict API")
        total_tests += 1
        try:
            payload = {
                "event1": "Board Meeting",
                "event2": "Family Time",
                "priority": "event1",
                "email": "Have a conflict"
            }
            resp = client.post('/resolve', 
                json=payload,
                content_type='application/json')
            if resp.status_code == 200:
                print(f"    [OK] /resolve -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /resolve -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 7: Emotion Analysis
        print("\n[7] Emotion Analysis API")
        total_tests += 1
        try:
            payload = {"text": "I'm so angry about this!"}
            resp = client.post('/emotion',
                json=payload,
                content_type='application/json')
            if resp.status_code == 200:
                print(f"    [OK] /emotion -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /emotion -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 8: Rewrite Message
        print("\n[8] Rewrite Message API")
        total_tests += 1
        try:
            payload = {
                "message": "This is terrible!",
                "llm_level": "advanced"
            }
            resp = client.post('/rewrite',
                json=payload,
                content_type='application/json')
            if resp.status_code == 200:
                print(f"    [OK] /rewrite -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /rewrite -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 9: Mediate Conflict
        print("\n[9] Mediate Conflict API")
        total_tests += 1
        try:
            payload = {
                "side_a": "We need to finish the project",
                "side_b": "We need to maintain quality",
                "shared_goal": "Successful project delivery"
            }
            resp = client.post('/mediate',
                json=payload,
                content_type='application/json')
            if resp.status_code == 200:
                print(f"    [OK] /mediate -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /mediate -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 10: History
        print("\n[10] Chat History API")
        total_tests += 1
        try:
            resp = client.get('/history')
            if resp.status_code == 200:
                print(f"    [OK] /history -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /history -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 11: Judging Readiness
        print("\n[11] Judging Readiness API")
        total_tests += 1
        try:
            resp = client.get("/api/judging/readiness")
            data = resp.get_json() or {}
            r = data.get("readiness") or {}
            if resp.status_code == 200 and "openenv_usage" in r and "reward_summary" in data:
                print("    [OK] /api/judging/readiness -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /api/judging/readiness -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 12: Agent Capabilities
        print("\n[12] Agent Capabilities API")
        total_tests += 1
        try:
            resp = client.get("/api/agent/capabilities")
            data = resp.get_json() or {}
            if resp.status_code == 200 and "core_modules" in data and "advanced_features" in data:
                print("    [OK] /api/agent/capabilities -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /api/agent/capabilities -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 13: What-If Simulate
        print("\n[13] What-If Simulation API")
        total_tests += 1
        try:
            payload = {
                "scenario": "Reschedule a meeting with two conflicting requests",
                "options": ["Postpone to tomorrow", "Shorten the slot", "Delegate to colleague"]
            }
            resp = client.post("/api/whatif-simulate", json=payload, content_type="application/json")
            data = resp.get_json() or {}
            if resp.status_code == 200 and "ranked_outcomes" in data:
                print("    [OK] /api/whatif-simulate -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /api/whatif-simulate -> {resp.status_code} {data}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 14: Communication Script
        print("\n[14] Communication Script API")
        total_tests += 1
        try:
            payload = {
                "audience": "manager",
                "objective": "Request deadline extension",
                "context": "Project slipped due to illness",
            }
            resp = client.post("/api/communication-script", json=payload, content_type="application/json")
            data = resp.get_json() or {}
            if resp.status_code == 200 and "script" in data:
                print("    [OK] /api/communication-script -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /api/communication-script -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 15: Ethical Filter
        print("\n[15] Ethical Filter API")
        total_tests += 1
        try:
            payload = {"decision": "Decline a low-priority meeting", "context": "Time conflict with family commitment"}
            resp = client.post("/api/ethical-filter", json=payload, content_type="application/json")
            if resp.status_code == 200:
                print("    [OK] /api/ethical-filter -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /api/ethical-filter -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 16: Feedback Loop
        print("\n[16] Feedback Loop API")
        total_tests += 1
        try:
            payload = {
                "action": "reschedule",
                "outcome": "stakeholder agreed",
                "feedback": "Smooth outcome",
                "rating": 0.8
            }
            resp = client.post("/api/feedback-loop", json=payload, content_type="application/json")
            if resp.status_code == 200:
                print("    [OK] /api/feedback-loop -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /api/feedback-loop -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Test 17: Feedback Loop Summary
        print("\n[17] Feedback Loop Summary API")
        total_tests += 1
        try:
            resp = client.get("/api/feedback-loop/summary")
            data = resp.get_json() or {}
            if resp.status_code == 200 and "entries" in data:
                print("    [OK] /api/feedback-loop/summary -> 200 OK")
                success_count += 1
            else:
                print(f"    [FAIL] /api/feedback-loop/summary -> {resp.status_code}")
        except Exception as e:
            print(f"    [FAIL] Error: {e}")
        
        # Summary
        print("\n" + "=" * 70)
        print(f"RESULTS: {success_count}/{total_tests} tests passed")
        print("=" * 70)
        
        if success_count == total_tests:
            print("\n[OK] ALL TESTS PASSED!")
            print("\n[OK] Frontend is ready to use!")
            print("   -> Open frontend/frontend.html in your browser")
            print("   -> Backend running at http://localhost:5000")
            return True
        else:
            print(f"\n[WARN] {total_tests - success_count} test(s) failed")
            print("   -> Check error messages above")
            return False

if __name__ == "__main__":
    success = test_frontend_integration()
    sys.exit(0 if success else 1)
