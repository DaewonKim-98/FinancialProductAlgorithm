<template>
  <div>
    <div class="map_wrap">
      <div class="d-flex justify-content-center">
        <form @submit.prevent="searchPlaces">
          <div class="d-flex m-5">
            <label for="지역명" class="d-flex me-5">
              <p class="m-1 me-3 fw-bold fs-4">지역 :</p>
              <input v-model="keyword1" type="text" id="지역명" class="fs-4 border border-warning border-3">
            </label>
            <label for="지역명" class="d-flex">
              <p class="m-1 me-3 fw-bold fs-4">은행명 :</p>
              <input v-model="keyword2" type="text" id="지역명" class="fs-4 border border-warning border-3">
            </label>
            <button type="submit" class="fs-4 ms-5 btn btn-warning px-3">검색</button>
          </div>
        </form>
      </div>
      <div id="map" style="width: 100%; height: 130%; position: relative; overflow: hidden;"></div>

      <div id="menu_wrap" class="bg_white" style="margin-top: 130px;">

        <hr />
        <ul id="placesList">
          <li v-for="(place, index) in places" :key="index" class="item">
            <span :class="['markerbg', 'marker_' + (index + 1)]"></span>
            <div class="info">
              <h5>{{ place.place_name }}</h5>
              <span v-if="place.road_address_name">{{ place.road_address_name }}</span>
              <span class="jibun gray">{{ place.address_name }}</span>
              <span class="tel">{{ place.phone }}</span>
            </div>
          </li>
        </ul>
        <div class="" id="pagination"></div>
      </div>
    </div>
  </div>
</template>

<script>
const API_KEY = import.meta.env.VITE_KAKAO_API

export default {
  data() {
    return {
      map: null,
      infowindow: null,
      keyword1: '역삼역',
      keyword2: '은행',
      keyword: "역삼역 은행",
      places: [],
    };
  },
  mounted() {
    const script = document.createElement("script");
    script.type = "text/javascript";
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${API_KEY}&libraries=services&autoload=false`;
    document.head.appendChild(script);

    script.onload = () => {
      kakao.maps.load(() => {
        this.initMap();
      });
    };
  },
  methods: {
    initMap() {
      const container = document.getElementById("map");
      const options = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567),
        level: 3,
      };
      this.map = new kakao.maps.Map(container, options);
      this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

      this.searchPlaces();
    },
    searchPlaces() {
      const ps = new kakao.maps.services.Places();
      const keyword = this.keyword1 + ' ' + this.keyword2
      ps.keywordSearch(keyword, this.placesSearchCB);
    },

    placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
        this.displayPlaces(data);
        this.displayPagination(pagination);
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert("검색 결과가 존재하지 않습니다.");
      } else if (status === kakao.maps.services.Status.ERROR) {
        alert("검색 결과 중 오류가 발생했습니다.");
      }
    },

    displayPlaces(places) {
      // 이전 마커 제거
      this.removeMarker();

      this.places = places;

      const bounds = new kakao.maps.LatLngBounds();
      places.forEach((place, index) => {
        const placePosition = new kakao.maps.LatLng(place.y, place.x);
        const marker = this.addMarker(placePosition, index);
        bounds.extend(placePosition);

        kakao.maps.event.addListener(marker, "mouseover", () => {
          this.displayInfowindow(marker, place.place_name);
        });

        kakao.maps.event.addListener(marker, "mouseout", () => {
          this.infowindow.close();
        });
      });

      this.map.setBounds(bounds);
    },
    displayInfowindow(marker, title) {
      const content = `<div style="padding:5px;z-index:1;">${title}</div>`;
      this.infowindow.setContent(content);
      this.infowindow.open(this.map, marker);
    },
    displayPagination(pagination) {
      const paginationEl = document.getElementById("pagination");
      const fragment = document.createDocumentFragment();

      while (paginationEl.hasChildNodes()) {
        paginationEl.removeChild(paginationEl.lastChild);
      }

      for (let i = 1; i <= pagination.last; i++) {
        const el = document.createElement("a");
        el.href = "#";
        el.innerHTML = i;

        if (i === pagination.current) {
          el.className = "on";
        } else {
          el.onclick = () => {
            pagination.gotoPage(i);
          };
        }

        fragment.appendChild(el);
      }

      paginationEl.appendChild(fragment);
    },
    addMarker(position, idx) {
      const imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png";
      const imageSize = new kakao.maps.Size(36, 37);
      const imgOptions = {
        spriteSize: new kakao.maps.Size(36, 691),
        spriteOrigin: new kakao.maps.Point(0, idx * 46 + 10),
        offset: new kakao.maps.Point(13, 37),
      };
      const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions);
      const marker = new kakao.maps.Marker({
        position: position,
        image: markerImage,
      });

      marker.setMap(this.map);
      this.places[idx] = { ...this.places[idx], marker: marker };

      return marker;
    },
    removeMarker() {
      this.places.forEach((place) => {
        if (place.marker) {
          place.marker.setMap(null);
        }
      });
    },
  },
};
</script>

<style scoped>
.map_wrap,
.map_wrap * {
  margin: 0;
  padding: 0;
  font-family: "Malgun Gothic", dotum, "돋움", sans-serif;
  font-size: 12px;
}
.map_wrap a,
.map_wrap a:hover,
.map_wrap a:active {
  color: #000;
  text-decoration: none;
}
.map_wrap {
  position: relative;
  width: 100%;
  height: 500px;
}
#menu_wrap {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 250px;
  margin: 10px 0 30px 10px;
  padding: 5px;
  overflow-y: auto;
  background: rgba(255, 255, 255, 0.7);
  z-index: 1;
  font-size: 12px;
  border-radius: 10px;
}
.bg_white {
  background: #fff;
}
#menu_wrap hr {
  display: block;
  height: 1px;
  border: 0;
  border-top: 2px solid #5f5f5f;
  margin: 3px 0;
}
#menu_wrap .option {
  text-align: center;
}
#menu_wrap .option p {
  margin: 10px 0;
}
#menu_wrap .option button {
  margin-left: 5px;
}
#placesList li {
  list-style: none;
}
#placesList .item {
  position: relative;
  border-bottom: 1px solid #888;
  overflow: hidden;
  cursor: pointer;
  min-height: 65px;
}
#placesList .item span {
  display: block;
  margin-top: 4px;
}
#placesList .item h5,
#placesList .item .info {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
#placesList .item .info {
  padding: 10px 0 10px 55px;
}
#placesList .info .gray {
  color: #8a8a8a;
}
#placesList .info .jibun {
  padding-left: 26px;
  background: url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;
}
#placesList .info .tel {
  color: #009900;
}
#placesList .item .markerbg {
  float: left;
  position: absolute;
  width: 36px;
  height: 37px;
  margin: 10px 0 0 10px;
  background: url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat;
}
#placesList .item .marker_1 {
  background-position: 0 -10px;
}
#placesList .item .marker_2 {
  background-position: 0 -56px;
}
#placesList .item .marker_3 {
  background-position: 0 -102px;
}
#placesList .item .marker_4 {
  background-position: 0 -148px;
}
#placesList .item .marker_5 {
  background-position: 0 -194px;
}
#placesList .item .marker_6 {
  background-position: 0 -240px;
}
#placesList .item .marker_7 {
  background-position: 0 -286px;
}
#placesList .item .marker_8 {
  background-position: 0 -332px;
}
#placesList .item .marker_9 {
  background-position: 0 -378px;
}
#placesList .item .marker_10 {
  background-position: 0 -423px;
}
#placesList .item .marker_11 {
  background-position: 0 -470px;
}
#placesList .item .marker_12 {
  background-position: 0 -516px;
}
#placesList .item .marker_13 {
  background-position: 0 -562px;
}
#placesList .item .marker_14 {
  background-position: 0 -608px;
}
#placesList .item .marker_15 {
  background-position: 0 -654px;
}
#pagination {
  margin: 10px auto;
  text-align: center;
  font-size: 15px;
}
#pagination a {
  display: inline-block;
  margin-right: 0px;
}
#pagination .on {
  font-weight: bold;
  cursor: default;
  color: #777;
}
</style>
