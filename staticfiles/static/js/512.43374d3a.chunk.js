"use strict";(self.webpackChunkfrontend=self.webpackChunkfrontend||[]).push([[512],{2444:function(e,t,s){var n=s(5861),r=s(7757),a=s.n(r),i=s(6871),l=s(2806),o=s(184);t.Z=function(e){var t=(0,i.s0)(),s=!!localStorage.getItem("authTokens"),r=function(){var r=(0,n.Z)(a().mark((function n(r){var i;return a().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:if(r.stopPropagation(),s){n.next=5;break}t("/login"),n.next=10;break;case 5:return n.next=7,l.Z.post("follow-request/",{user:e.user.id});case 7:201===(i=n.sent).status&&(e.setFollow(!0),e.setFollowWasSuc(i.data.id));case 10:case"end":return n.stop()}}),n)})));return function(e){return r.apply(this,arguments)}}();return(0,o.jsx)("button",{className:"btn",type:"submit",style:{backgroundColor:e.backgroundColor,color:e.color},onClick:r,children:"Follow"})}},1689:function(e,t,s){var n=s(5861),r=s(7757),a=s.n(r),i=(s(2791),s(6871)),l=s(2806),o=s(184);t.Z=function(e){var t=(0,i.s0)(),s=!!localStorage.getItem("authTokens"),r=function(){var r=(0,n.Z)(a().mark((function n(r){return a().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:if(r.stopPropagation(),s){n.next=5;break}t("/login"),n.next=9;break;case 5:return n.next=7,l.Z.post("like-tweet/".concat(e.tweetId));case 7:201===n.sent.status&&(e.setFakeLikeNumber((function(e){return e+1})),e.setLikeClicked(!0));case 9:case"end":return n.stop()}}),n)})));return function(e){return r.apply(this,arguments)}}();return(0,o.jsxs)("div",{children:[(0,o.jsx)("i",{className:"fa fa-heart-o",onClick:r}),(0,o.jsx)("p",{children:e.likes})]})}},5810:function(e,t,s){s(4164);var n=s(184),r=function(e){return(0,n.jsx)("div",{className:"error_message__container",children:(0,n.jsxs)("div",{className:"error-message__modal",children:[e.errorMessage,(0,n.jsx)("div",{children:(0,n.jsx)("button",{className:"btn",onClick:e.onClose,children:"Close"})})]})})};document.getElementById("root"),t.Z=r},4312:function(e,t,s){var n=s(5861),r=s(7757),a=s.n(r),i=s(2791),l=s(3504),o=s(29),c=s(5854),u=s(654),d=s(2806),f=s(184);t.Z=function(e){var t=(0,i.useRef)(""),s=(0,i.useContext)(u.V).userData;function r(){return(r=(0,n.Z)(a().mark((function s(){var n;return a().wrap((function(s){for(;;)switch(s.prev=s.next){case 0:return s.next=2,d.Z.post("tweets/".concat(e.tweetId,"/reply"),{text:t.current.value});case 2:if(201!==(n=s.sent).status){s.next=7;break}return e.setNewReply(n.data.id),t.current.value="",s.abrupt("return");case 7:case"end":return s.stop()}}),s)})))).apply(this,arguments)}return(0,f.jsxs)("div",{className:o.Z["reply-section"],children:[(0,f.jsx)("div",{className:o.Z["close-reply__section"],children:(0,f.jsx)("i",{className:"fa fa-times","aria-hidden":"true",onClick:function(){return e.hideReply()},style:{cursor:"pointer"}})}),(0,f.jsxs)("div",{className:o.Z.user__info,children:[(0,f.jsx)("div",{className:o.Z["user-info__left"],children:(0,f.jsx)("img",{src:e.picture,alt:"Profile"})}),(0,f.jsxs)("div",{className:o.Z["user-info__right"],children:[(0,f.jsxs)("div",{className:o.Z.user__names,children:[(0,f.jsx)("p",{id:o.Z.fullname,children:"".concat(e.firstname," ").concat(e.lastname)}),(0,f.jsx)("p",{id:o.Z.username,children:e.username}),(0,f.jsx)("p",{children:"\xb7"}),(0,f.jsx)("p",{id:o.Z["time-created"],children:e.timeCreated})]}),(0,f.jsx)("div",{className:o.Z["tweet-content"],children:e.content})]})]}),(0,f.jsxs)("form",{id:"add-reply",className:o.Z["add-reply__form"],onSubmit:function(n){n.preventDefault(),s?t.current.value.trim().length>0&&function(){r.apply(this,arguments)}():e.onError((0,f.jsxs)("p",{children:["Please ",(0,f.jsx)(l.rU,{to:"/login",children:"login"})," before adding a tweet."]}))},children:[(0,f.jsxs)("div",{className:o.Z["add-reply__upper"],children:[s?(0,f.jsx)("img",{className:o.Z["add-reply__image"],src:s.picture,alt:"Default profile"}):(0,f.jsx)("img",{className:o.Z["add-reply__image"],src:c,alt:"Default profile"}),(0,f.jsx)("textarea",{className:o.Z["add-reply__input"],placeholder:"Tweet your reply",ref:t,name:"reply"})]}),(0,f.jsx)("div",{className:o.Z["add-reply__lower"],children:(0,f.jsx)("div",{className:o.Z["btn-container"],children:(0,f.jsx)("button",{className:"btn",type:"submit",children:"Reply"})})})]})]})}},1684:function(e,t,s){var n=s(5861),r=s(885),a=s(7757),i=s.n(a),l=s(2791),o=s(6871),c=s(2806),u=s(184);t.Z=function(e){var t=(0,o.s0)(),s=!!localStorage.getItem("authTokens"),a=(0,l.useState)(null),d=(0,r.Z)(a,2),f=d[0],_=d[1],p=(0,l.useState)(!1),m=(0,r.Z)(p,2),h=m[0],x=m[1],g=(0,l.useState)(!1),k=(0,r.Z)(g,2),j=k[0],w=k[1],Z=(0,l.useState)(null),v=(0,r.Z)(Z,2),y=v[0],b=v[1],N=(0,l.useCallback)((0,n.Z)(i().mark((function t(){return i().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,c.Z.get("bookmarks/".concat(e.tweetId,"/check"));case 3:200===t.sent.status&&_(!0),t.next=11;break;case 7:t.prev=7,t.t0=t.catch(0),console.clear(),404===t.t0.response.status&&_(!1);case 11:case"end":return t.stop()}}),t,null,[[0,7]])}))),[e.tweetId]);(0,l.useEffect)((function(){s?(x(!0),N(),w(!0)):(x(!0),w(!0))}),[y,N,s]);var C=function(){var r=(0,n.Z)(i().mark((function n(r){return i().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return r.stopPropagation(),s||t("/login"),n.next=4,c.Z.post("tweets/".concat(e.tweetId,"/create-bookmark"));case 4:201===n.sent.status&&b(Date.now());case 6:case"end":return n.stop()}}),n)})));return function(e){return r.apply(this,arguments)}}(),S=function(){var t=(0,n.Z)(i().mark((function t(s){return i().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return s.stopPropagation(),t.next=3,c.Z.delete("bookmarks/".concat(e.tweetId,"/delete"));case 3:204===t.sent.status&&(b(Date.now()),e.isBookmarkPage&&e.setNeedRefreshTweetList(Date.now()));case 5:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}();return f&&h&&j?(0,u.jsx)("i",{className:"fas fa-save fa-lg","aria-hidden":"true",onClick:S}):!f&&h&&j?(0,u.jsx)("i",{className:"far fa-save fa-lg","aria-hidden":"true",onClick:C}):void 0}},2333:function(e,t,s){s.d(t,{Z:function(){return j}});var n=s(2724),r=s(5861),a=s(885),i=s(7757),l=s.n(i),o=s(2791),c=s(6871),u=s(1689),d=s(1277),f=s(4312),_=s(5810),p=s(629),m=s(1684),h=s(2806),x=s(184),g=function(e){var t,s="#/get-profile/".concat(e.username),i=(0,c.s0)(),g=(0,o.useState)(!1),k=(0,a.Z)(g,2),j=k[0],w=k[1],Z=(0,o.useState)(!1),v=(0,a.Z)(Z,2),y=v[0],b=v[1],N=(0,o.useState)(null),C=(0,a.Z)(N,2),S=C[0],P=C[1],R=(0,o.useState)(null),I=(0,a.Z)(R,2),F=I[0],L=I[1],M=(0,o.useState)(e.likes),E=(0,a.Z)(M,2),T=E[0],B=E[1],D=!!localStorage.getItem("authTokens"),O=(0,o.useState)(!1),V=(0,a.Z)(O,2),W=V[0],Y=V[1],U=(0,o.useState)(!1),G=(0,a.Z)(U,2),H=G[0],q=G[1],X=(0,o.useState)(null),A=(0,a.Z)(X,2),K=A[0],J=A[1],z=(0,o.useState)(null),Q=(0,a.Z)(z,2)[1],$=function(){Y(!1),document.getElementById("add-reply__container").classList.add("hidden")},ee=function(){var t=(0,r.Z)(l().mark((function t(){return l().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(b(!0),w(!0),!D){t.next=5;break}return t.next=5,h.Z.get("like/".concat(e.tweetId,"/check")).then((function(e){if(200!==e.status)throw e.status;P((0,x.jsx)(d.Z,{likeId:e.data.id,likes:T,setFakeLikeNumber:B,setLikeClicked:L}))})).catch((function(){console.clear(),P((0,x.jsx)(u.Z,{tweetId:e.tweetId,likes:T,setFakeLikeNumber:B,setLikeClicked:L}))}));case 5:w(!1);case 6:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}();(0,o.useEffect)((function(){ee()}),[F]),t=D?(0,x.jsx)("div",{title:"Like",children:!j&&y&&S}):(0,x.jsxs)("div",{title:"Like",children:[(0,x.jsx)("i",{className:"fa fa-heart-o",onClick:function(){return i("/login")}}),(0,x.jsx)("p",{children:e.likes})]});return(0,x.jsxs)(o.Fragment,{children:[H&&(0,x.jsx)(_.Z,{errorMessage:K,onClose:function(){J(null),q(!1)}}),(0,x.jsx)(p.Z,{isVisible:W,onOverlayClick:function(){return $()}}),(0,x.jsx)("section",{id:"add-reply__container",className:"add-reply__container hidden",children:(0,x.jsx)(f.Z,{onError:function(e){J(e),q(!0)},tweetId:e.tweetId,username:e.user,firstname:e.firstname,lastname:e.lastname,timeCreated:e.timeCreated,picture:e.picture,content:e.content,hideReply:$,setNewReply:Q})}),(0,x.jsxs)("div",{className:n.Z.tweet,onClick:function(){i("/tweets/".concat(e.tweetId))},children:[(0,x.jsx)("div",{className:n.Z["tweet-left"],children:(0,x.jsx)("img",{src:e.picture,alt:"Profile",style:{objectFit:"cover"}})}),(0,x.jsxs)("div",{className:n.Z["tweet-right"],children:[(0,x.jsx)("div",{className:n.Z["tweet-right__top"],children:(0,x.jsxs)("div",{className:n.Z["user-info"],children:[(0,x.jsxs)("a",{id:n.Z["user-name"],href:s,children:[e.firstname," ",e.lastname]}),(0,x.jsx)("a",{id:n.Z.username,href:s,children:e.username}),(0,x.jsx)("a",{id:n.Z["tweet-dot"],href:s,children:"\xb7"}),(0,x.jsx)("a",{id:n.Z["tweet__time-created"],href:s,children:e.timeCreated})]})}),(0,x.jsx)("div",{className:n.Z["tweet-content"],children:e.content}),(0,x.jsxs)("div",{className:n.Z["tweet-right__bottom"],children:[(0,x.jsxs)("div",{title:"Reply",onClick:function(e){e.stopPropagation(),Y(!0),document.getElementById("add-reply__container").classList.remove("hidden")},children:[(0,x.jsx)("i",{className:"fa fa-reply"}),(0,x.jsx)("p",{children:e.reply})]}),t,(0,x.jsx)("div",{title:"Save",children:(0,x.jsx)(m.Z,{tweetId:e.tweetId,setHasError:q,setErrorMessage:J,setNeedRefreshTweetList:e.setNeedRefresh,isBookmarkPage:e.isBookmarkPage})})]})]})]})]})},k=s(4457),j=function(e){return e.tweetList?(0,x.jsx)("section",{id:"tweet-list",className:n.Z["tweet-list"],children:0!==e.tweetList.length?e.tweetList.map((function(t){return(0,x.jsx)(g,{tweetId:t.id,firstname:t.user.firstname,lastname:t.user.lastname,username:t.user.username,picture:t.user.picture,timeCreated:(0,k.Z)(t.date_created.created_ago,t.date_created.created),content:t.content,reply:t.tweetReply,retweet:t.tweetRetweets,likes:t.likes.length,isBookmarkPage:e.isBookmarkPage,setNeedRefresh:e.setNeedRefresh},t.id)})):(0,x.jsx)("p",{className:"p-info--center",children:"No posts yet!"})}):(0,x.jsx)("section",{className:n.Z["no-tweet"],children:(0,x.jsx)("p",{children:"No tweet was found, Please check your internet connection."})})}},5724:function(e,t,s){var n=s(5861),r=s(7757),a=s.n(r),i=s(6871),l=s(2806),o=s(184);t.Z=function(e){var t=(0,i.s0)(),s=!!localStorage.getItem("authTokens"),r=function(){var r=(0,n.Z)(a().mark((function n(r){var i;return a().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:if(r.stopPropagation(),s){n.next=5;break}t("/login"),n.next=15;break;case 5:if("followings"!==e.pageName&&"followers"!==e.pageName){n.next=11;break}return n.next=8,l.Z.delete("unfollow/".concat(e.username));case 8:i=n.sent,n.next=14;break;case 11:return n.next=13,l.Z.delete("profiles/".concat(e.unfollowId,"/follow/delete"));case 13:i=n.sent;case 14:204===i.status&&e.setFollow(Date.now());case 15:case"end":return n.stop()}}),n)})));return function(e){return r.apply(this,arguments)}}();return(0,o.jsx)("button",{className:"btn",type:"submit",style:{backgroundColor:e.backgroundColor,color:e.color},onClick:r,children:"Unfollow"})}},1277:function(e,t,s){var n=s(5861),r=s(7757),a=s.n(r),i=(s(2791),s(6871)),l=s(2806),o=s(184);t.Z=function(e){var t=(0,i.s0)(),s=!!localStorage.getItem("authTokens"),r=function(){var r=(0,n.Z)(a().mark((function n(r){return a().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:if(r.stopPropagation(),s){n.next=5;break}t("/login"),n.next=9;break;case 5:return n.next=7,l.Z.delete("remove-like/".concat(e.likeId));case 7:204===n.sent.status&&(e.setFakeLikeNumber((function(e){return e-1})),e.setLikeClicked(!1));case 9:case"end":return n.stop()}}),n)})));return function(e){return r.apply(this,arguments)}}();return(0,o.jsxs)("div",{children:[(0,o.jsx)("i",{className:"fa fa-heart",style:{color:"red"},onClick:r}),(0,o.jsx)("p",{children:e.likes})]})}},4887:function(e,t,s){s.d(t,{Z:function(){return x}});var n=s(5861),r=s(885),a=s(7757),i=s.n(a),l=s(2791),o={"you-might-like":"YouMightLike_you-might-like__EVWFg","suggested-users":"YouMightLike_suggested-users__84w7p","suggested-user":"YouMightLike_suggested-user__bn1Rr","suggested-user__left":"YouMightLike_suggested-user__left__0dHxW",fullname:"YouMightLike_fullname__koNmx",username:"YouMightLike_username__ZbD+j"},c=s(4569),u=s.n(c),d=s(5854),f=s(2444),_=s(184),p=function(e){return(0,_.jsxs)("div",{className:o["suggested-user"],children:[(0,_.jsxs)("div",{className:o["suggested-user__left"],children:[(0,_.jsx)("img",{src:d,alt:"profile"}),(0,_.jsxs)("a",{className:o["user-info"],href:"#/get-profile/".concat(e.user.username),children:[(0,_.jsx)("p",{id:o.fullname,children:"".concat(e.user.firstname," ").concat(e.user.lastname)}),(0,_.jsxs)("p",{id:o.username,children:["@",e.user.username]})]})]}),(0,_.jsx)("div",{className:o["suggested-user__right"],children:(0,_.jsx)(f.Z,{color:"#fff",backgroundColor:"#000",user:e.user,setFollowWasSuc:e.setFollowWasSuc,setFollow:e.setFollow})})]})},m=s(6706),h=s(2806),x=function(){var e=(0,l.useState)([]),t=(0,r.Z)(e,2),s=t[0],a=t[1],c=!!localStorage.getItem("authTokens"),d=(0,l.useState)(null),f=(0,r.Z)(d,2),x=f[0],g=f[1],k=(0,l.useState)(null),j=(0,r.Z)(k,2),w=(j[0],j[1]),Z=(0,l.useContext)(m.S).serverURL,v=(0,l.useCallback)((0,n.Z)(i().mark((function e(){var t;return i().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(c){e.next=6;break}return e.next=3,u().get("".concat(Z,"suggested-users"));case 3:t=e.sent,e.next=9;break;case 6:return e.next=8,h.Z.get("".concat(Z,"suggested-users"));case 8:t=e.sent;case 9:200===t.status&&a(t.data);case 10:case"end":return e.stop()}}),e)}))),[c,Z]);return(0,l.useEffect)((function(){v()}),[x]),(0,_.jsxs)("section",{className:o["you-might-like"],children:[(0,_.jsx)("p",{children:"Who to follow"}),(0,_.jsxs)("div",{className:o["suggested-users"],children:[s.length>0&&s.map((function(e){return(0,_.jsx)(p,{user:e,setFollowWasSuc:g,setFollow:w},e.id)})),0===s.length&&(0,_.jsx)("p",{style:{color:"black",textAlign:"center",fontWeight:"bold"},children:"No Suggested users"})]})]})}},3512:function(e,t,s){s.r(t),s.d(t,{default:function(){return y}});var n=s(5861),r=s(885),a=s(7757),i=s.n(a),l=s(4887),o=s(2791),c=s(2333),u=s(1422),d=s(6871),f=s(2444),_=s(1566),p=s(4457),m=s(5724),h=s(629),x=s(654),g=s(2806),k=s(184),j=function(e){var t=(0,d.s0)(),s=(0,o.useState)(!1),a=(0,r.Z)(s,2),l=a[0],c=a[1],u=(0,o.useState)(!1),j=(0,r.Z)(u,2),w=j[0],Z=j[1],v=(0,o.useState)(null),y=(0,r.Z)(v,2),b=y[0],N=y[1],C=(0,o.useContext)(x.V).user,S=function(){var s=(0,n.Z)(i().mark((function s(){return i().wrap((function(s){for(;;)switch(s.prev=s.next){case 0:if(Z(!0),c(!0),!C){s.next=9;break}if(C.username!==e.user.username){s.next=7;break}N((0,k.jsx)("button",{className:"btn",onClick:function(){return t("/edit/".concat(C.username))},children:"Edit profile"})),s.next=9;break;case 7:return s.next=9,g.Z.get("follow/".concat(e.user.username,"/check")).then((function(t){if(200!==t.status)throw t.status;N((0,k.jsx)(m.Z,{unfollowId:t.data.id,setFollow:e.setFollow}))})).catch((function(){N((0,k.jsx)(f.Z,{user:e.user,setFollow:e.setFollow})),console.clear()}));case 9:c(!1);case 10:case"end":return s.stop()}}),s)})));return function(){return s.apply(this,arguments)}}();return(0,o.useEffect)((function(){S()}),[]),(0,k.jsxs)("section",{className:_.Z.profile,children:[e.isMenuOpen?(0,k.jsx)(h.Z,{onOverlayClick:e.onOverlayClick,isVisible:!0}):(0,k.jsx)(h.Z,{onOverlayClick:e.onOverlayClick,isVisible:!1}),(0,k.jsxs)("div",{className:_.Z.profile__top,children:[(0,k.jsxs)("div",{className:_.Z["profile__top-left"],children:[(0,k.jsxs)("div",{className:"ham-menu__btn",id:_.Z["ham-menu__btn"],onClick:e.onMenuClick,children:[(0,k.jsx)("div",{}),(0,k.jsx)("div",{}),(0,k.jsx)("div",{})]}),(0,k.jsxs)("div",{children:[(0,k.jsx)("h3",{children:"".concat(e.user.firstname," ").concat(e.user.lastname)}),(0,k.jsxs)("p",{children:[e.user.tweet_number," Tweets"]})]})]}),(0,k.jsx)("div",{})]}),(0,k.jsx)("img",{src:e.user.background_picture,alt:"header"}),(0,k.jsxs)("div",{className:_.Z.profile__bottom,children:[(0,k.jsxs)("div",{className:_.Z["profile__bottom-middle"],children:[(0,k.jsx)("img",{src:e.user.picture,alt:"profile"}),!l&&w&&b]}),(0,k.jsxs)("div",{className:_.Z["profile__bottom-bottom"],children:[(0,k.jsxs)("div",{className:_.Z["user-info"],children:[(0,k.jsx)("h3",{children:"".concat(e.user.firstname," ").concat(e.user.lastname)}),(0,k.jsxs)("p",{children:["@",e.user.username]})]}),(0,k.jsx)("div",{className:_.Z["user-bio"],children:(0,k.jsx)("p",{children:e.user.bio})}),(0,k.jsxs)("p",{className:_.Z["user-date-joined"],children:["Joined"," ",(0,p.Z)(e.user.date_joined.date_joined_ago,e.user.date_joined.date_joined)]}),(0,k.jsxs)("div",{className:_.Z.follow,children:[(0,k.jsxs)("div",{className:_.Z["user-follow"],onClick:function(){return t("/".concat(e.user.username,"/followings"))},children:[(0,k.jsx)("span",{children:e.user.follows.followings_count}),(0,k.jsx)("p",{id:_.Z["user-follow__text"],children:"Following"})]}),(0,k.jsxs)("div",{className:_.Z["user-follow"],onClick:function(){return t("/".concat(e.user.username,"/followers"))},children:[(0,k.jsx)("span",{children:e.user.follows.followers_count}),(0,k.jsx)("p",{id:_.Z["user-follow__text"],children:"Followers"})]})]})]})]})]})},w=s(4569),Z=s.n(w),v=s(6706),y=function(e){var t=(0,o.useState)(null),s=(0,r.Z)(t,2),a=s[0],f=s[1],_=!!localStorage.getItem("authTokens"),p=(0,o.useState)(!1),m=(0,r.Z)(p,2),h=m[0],x=m[1],w=(0,o.useState)(!1),y=(0,r.Z)(w,2),b=y[0],N=y[1],C=(0,o.useState)(null),S=(0,r.Z)(C,2),P=S[0],R=S[1],I=(0,d.UO)().username,F=(0,o.useState)(null),L=(0,r.Z)(F,2),M=L[0],E=L[1],T=(0,o.useState)([]),B=(0,r.Z)(T,2),D=B[0],O=B[1],V=(0,o.useState)(!1),W=(0,r.Z)(V,2),Y=W[0],U=W[1],G=(0,o.useState)(!1),H=(0,r.Z)(G,2),q=H[0],X=H[1],A=(0,o.useState)(!1),K=(0,r.Z)(A,2),J=K[0],z=K[1],Q=(0,o.useContext)(v.S).serverURL,$=function(){var e=(0,n.Z)(i().mark((function e(){return i().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(N(!0),x(!0),_){e.next=5;break}return e.next=5,Z().get("".concat(Q,"profiles/").concat(I)).then((function(e){return f(e.data)})).catch((function(e){return R(e)}));case 5:if(!_){e.next=8;break}return e.next=8,g.Z.get("profiles/".concat(I)).then((function(e){return f(e.data)})).catch((function(e){return R(e)}));case 8:x(!1);case 9:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),ee=function(){var e=(0,n.Z)(i().mark((function e(){return i().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return X(!0),U(!0),e.next=4,Z().get("".concat(Q,"profiles/").concat(I,"/tweets")).then((function(e){200===e.status&&O(e.data)})).catch((function(){return z(!0)}));case 4:U(!1);case 5:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();return(0,o.useEffect)((function(){$(),ee()}),[M,I]),(0,k.jsxs)(o.Fragment,{children:[(0,k.jsxs)("div",{className:"main__middle-side",children:[!P&&!h&&b&&(0,k.jsx)(j,{user:a,setFollow:E,isMenuOpen:e.isMenuOpen,onOverlayClick:function(){e.onMenuClick()},onMenuClick:e.onMenuClick}),b&&P&&(0,k.jsx)("section",{className:"profile-not-found",children:(0,k.jsx)("p",{className:"p-info--center",style:{marginTop:"0"},children:"Sorry this profile doesn't exist."})}),q&&!Y&&!J&&(0,k.jsx)(c.Z,{isBookmarkPage:!1,tweetList:D}),q&&!Y&&!J&&0===D.length&&(0,k.jsx)("p",{className:"p-info--center",children:"No tweets from this profile yet!"})]}),(0,k.jsxs)("div",{className:"main__right-side",children:[(0,k.jsx)(u.Z,{}),(0,k.jsx)(l.Z,{})]})]})}},1566:function(e,t){t.Z={profile:"Profile_profile__4ECaZ",profile__top:"Profile_profile__top__-5nvg","ham-menu__btn":"Profile_ham-menu__btn__s+Er+",profile__bottom:"Profile_profile__bottom__wGa-q","profile__top-left":"Profile_profile__top-left__RFx7D",icon:"Profile_icon__Pibt-","profile__bottom-middle":"Profile_profile__bottom-middle__UKVWd","profile__bottom-bottom":"Profile_profile__bottom-bottom__XxSuW","user-info":"Profile_user-info__MkZP6","user-date-joined":"Profile_user-date-joined__GKI9R",follow:"Profile_follow__p3ag8","user-follow":"Profile_user-follow__Gx9sB","profile-list":"Profile_profile-list__YPDBx","small-profile__section":"Profile_small-profile__section__Gm7m8","small-profile__left-part":"Profile_small-profile__left-part__5fF3j","small-profile__right-part":"Profile_small-profile__right-part__+jHGE","small-profile__right-top":"Profile_small-profile__right-top__VeD1w","small-profile__user-name":"Profile_small-profile__user-name__HH9Yf","small-profile__fullname":"Profile_small-profile__fullname__SBS06","small-profile__username":"Profile_small-profile__username__UDzsT","small-profile__right-bottom":"Profile_small-profile__right-bottom__RWSFb"}},29:function(e,t){t.Z={"reply-section":"Reply_reply-section__BbnCc",user__info:"Reply_user__info__UitVu","user-info__left":"Reply_user-info__left__qR7yp","user-info__right":"Reply_user-info__right__M3A23",user__names:"Reply_user__names__6lVy1","link--underline":"Reply_link--underline__IUIu6",fullname:"Reply_fullname__lqRK6","tweet-content":"Reply_tweet-content__GAg4T","add-reply__form":"Reply_add-reply__form__Y1WR7","add-reply__upper":"Reply_add-reply__upper__+Dp6b","add-reply__lower":"Reply_add-reply__lower__yX4-S","add-reply__image":"Reply_add-reply__image__MXGYn","add-reply__input":"Reply_add-reply__input__kTyOX","btn-container":"Reply_btn-container__+aEwk",hidden:"Reply_hidden__Z2HP2","reply-list":"Reply_reply-list__8iYMy",reply:"Reply_reply__4J+VP","reply-left":"Reply_reply-left__UpdBH","reply-right":"Reply_reply-right__V+8vO"}}}]);
//# sourceMappingURL=512.43374d3a.chunk.js.map