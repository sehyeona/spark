# Chapter 02 스파크 간단히 살펴보기
- - - 
### 2.1 스파크의 기본 아키텍처
> 한대의 컴퓨터는 대규모 연산을 수행할 만한 자원이나 성능이 부족하다. 
> 컴퓨터 *클러스터* 는 여러 컴퓨터의 자원을 모아 한대의 컴퓨터 처럼 사용하게 해준다.    
<br>
여기에는 클러스터(즉 컴퓨터 뭉치)에서 작업을 조율해줄 프레임워크가 필요한데 그것이 바로 *스파크* !
스파크가 연산에 사용할 클러스터는 스파크 스탠드얼론, 하둡 YARN, 메소스와 같은 클러스터 매니저에서 관리한다. 
> 사용자는 클러스터 매니저에게 *스파크 애플리케이션* 을 제출하고, 클러스터 매니저는 작업을 클러스터에 적절히 분배
#### 스파크 애플리케이션 = 드라이버프로세스 + 익스큐터 
1. 드라이버 : 스파크의 심장과 같은 존재, 하나의 클러스터에 위치하며, 애플리케이션의 수명 주기동안 관련 모든 정보를 저장
2. 익스큐터 : 드라이버 프로세스가 할당한 작업을 수행.   

<figure>
<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.edureka.co%2Fblog%2Fspark-architecture%2F&psig=AOvVaw1ekTE0Fj8-tdx9hjYt-A5X&ust=1591780129488000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLiYsKCx9OkCFQAAAAAdAAAAABAR" width=500 height = 200/> 
<figcaption>스파크 애플리케이션 아키텍처</figcaption>
</figure>
