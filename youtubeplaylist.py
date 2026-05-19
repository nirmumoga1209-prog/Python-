# YouTube Playlist Analyzer

def analyze_playlist(durations):
    """Analyze YouTube playlist and calculate various metrics"""
    
    if not durations:
        print("Playlist is empty!")
        return
    
    # Total watch time
    total_time = sum(durations)
    
    # Longest video
    longest = max(durations)
    
    # Average duration
    average = total_time / len(durations)
    
    # Videos shorter than 5 minutes
    short_videos = [d for d in durations if d < 5]
    
    # Display results
    print("=" * 50)
    print("YOUTUBE PLAYLIST ANALYSIS")
    print("=" * 50)
    print(f"Durations: {durations}")
    print()
    print(f"Total Watch Time: {total_time} minutes")
    print(f"Longest Video: {longest} minutes")
    print(f"Average Duration: {average:.2f} minutes")
    print(f"Videos Shorter than 5 Minutes: {short_videos}")
    print(f"Count of Short Videos: {len(short_videos)}")
    print("=" * 50)

# Sample Input
durations = [12, 4, 8, 15, 3, 20]
analyze_playlist(durations)

# Additional test case
print("\nAnother Playlist Example:")
durations2 = [5, 10, 2, 8, 3, 15, 6]
analyze_playlist(durations2)
