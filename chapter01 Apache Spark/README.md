# CHAPTER 01 아파치 스파크란

1. 아파치 스파크는 통합 컴퓨팅 엔진이며 클러스터 환경에서 데이터를 병렬로 처리하는 라이브러리 집합이다.    
2. 스파크는 가장 활발하게 개발되고 있는 병렬 처리 오픈소스 엔진이며 빅데이터에 관심 있는 여러 개발자와 데이터 과학자에게 표준 도구가 되어가고 있다.       
3. 스파크는 단일 노트북 환경에서부터 수천 대의 서버로 구성된 클러스터까지 다양한 환경에서 실행될 수 있다. 이런 특성을 활용해 빅데이터를 처리를 쉽게 시작할 수 있고 엄청난 규모의 클러스터로 확장해나갈 수 있다.   

[그림1]은 스파크에서 제공하는 전체 컴포넌트와 라이브러리이다.
<figure>
  <img src='https://m.media-amazon.com/images/S/aplus-media/vc/e6e4e247-7bf5-4090-9156-7a01aedd6acd.png' height="300px" width="450px" title="스파크 기능구성"/>
  <figcaption>[그림1] 스파크 기능 구성</figcaption>
</figure>

- - - 
### 1.1 아파치 스파크의 철학
아파치 스파크란 *'빅데이터를 위한 통합 컴퓨팅 엔진과 리이브러리 집합'* 이다. 
#### 통합
스파크는 *'빅데이터 애플리케이션 개발에 필요한 통합 플랫폼을 제공하자!'* 라는 핵심 목표를 가지고 있다.   
> 1. 스파크는 데이터읽기, SQL처리, 머신러닝, 스트림 처리까지 다양한 데이터 분석작업을 같은 연산엔진과 일관성 있는 API로 수행할 수 있도록 설계되었다.   
> 2. 실제로 데이터를 분석하기 위해 주피터나 전통 소프트웨어 개발에서는, 매우 다양한 라이브러리를 조합하고 연결하여 사용한다.   

=> 스파크의 통합 특성을 이용해 데이터 분석작업을 더쉽고 통합적으로 사용할 수 있게 한다.   
> 3. 스파크는 현재 *빅데이터 처리의 표준* 이다. 데이터 분석에 필요한 거의 모든 애플리케이션을 얻을 수 있다.   
또한 오픈소스로서 자체 API를 계속 확장해 나가고 있다.   
 #### 컴퓨팅 엔진
스파크는 통합이라는 관점을 중시하며 기능의 범위를 *컴퓨팅엔진* 으로 제한해왔다.    
=>  즉 자체적인 영구 저장소 역할은 전혀 수행하지 않으며, 데이터를 연산하는 역할만 한다.   
> 1. AWS, GCP 등의 클라우드 기반의 서비스/ Hadoop, Apache Casandra, kafka등의 분산 저장소를 지원한다. 
=> 대부분의 데이터는 여러 저장소에 분산 저장되어 있기 때문에, spark는 특정 저장소를 선호하지 않는다.   
> 2. 하둡 같은 경우에는 저장소(file system)와 컴퓨팅엔진(map reduce)가 매우 밀접하게 관련되어 있고, 분리하여 사용하기 어렵다. 
=> 스파크는 하둡 저장소와의 호환이 좋고 다양한 저장소에서 사용이 가능함.
#### 라이브러리
통합 API를 제공하는 *통합 엔진 기반의 자체 라이브러리* 가 스파크의 꽃이다.   
> 1. 스파크에서 자체 제공하는 표준 라이브러리
> 2. 외부에서 제공하는 서드파티 라이브러리  
> 3. 스파크 SQL, 스파크 MLLIB, 스파크 Streaming등 라이브러리와, 다양한 저장소 시스템을 위한 커넥터 부터 수백개의 외부 라이브러리 존재.
- - - 
### 1.2 스파크의 등장 배경 
1. 역사적으로 컴퓨터는 프로세서 성능 향상에 힘입에 해마다 빨라졌고 그에 따라 애플리케이션 성능도 자동적으로 좋아졌다. 
2. 하지만 2005년경 이후로 단일 코어의 성능은 정체되어 있다.(물리적인 방열한계)   
3. 따라서 하드웨어 개발자는 단일 코어보다 멀티 코어를 위주로 설계하게 되고, 이러한 현상을 병렬처리가 가능한 새로운 프로그래밍 모델이 세상에 도래할 것임을 암시했다.  
4. 반면 프로세서 속도는 정체된것에 비해 저장과 수집 기술은 거의 14개월마다 비용이 절반 이하로 줄어들고, 대용량의 데이터를 수집하는 기술은 해마다 진보한다.   
> 결과적으로 데이터 수집 비용은 극히 저렴하지만. 데이터는 클러스터에서 처리해야 할 만큼 거대해졌다. 따라서 새로운 프로그래밍 모델이 필요했으며, 아파치 스파크가 탄생하였다.
- - - 
### 1.3 스파크의 역사
UC버클리 스파크 연구 프로젝트로 시작되었다.
1. 클러스터 컴퓨팅이 엄청난 잠재력을 가지고 있는 것을 확인
2. 하지만 당시 클러스터의 1인자인 하둡은 난이도와 효율성에 문제가 있었다. 
스파크가 탄생하고 초기에는 *함수형 연산* (자바 객체, 맵리듀스 이용)에서 *구조화된 데이터* 를 기반으로 동작하는 API탄생
이후 여러 API가 끊임없이 추가되어 현재의 spark 탄생 
- - - 
### 1.4 스파크의 현재와 미래
거대한 규모의 데이터를 처리하기 위해 활발하게 사용되고 있다. 매우 빠르게 성장하고 있다는 점을 고려하면 빅데이터 분석을 수행하는 기업의 핵심 기술이 될것임을 예상할 수 있다.
