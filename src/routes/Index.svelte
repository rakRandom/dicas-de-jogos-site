<script>
// @ts-nocheck

    // Todo: Security test (text overflow, layout overflow, right position, responsivity etc)
    // Todo: Responsivity (follow mobile-first principles)
    // Todo: Add Black and White themes
    // Todo: Add class "uppercase" to the titles that need all the letters to be uppercase

    import { title }     from '.././stores.js';
    import Header        from '.././components/Header.svelte';
    import MainArticle   from '.././components/landing_page/MainArticle.svelte';
    import SimpleSection from '.././components/SimpleSection.svelte';
    import BulletTipItem from '.././components/landing_page/BulletTipItem.svelte';
    import PopUpArticle  from '.././components/PopUpArticle.svelte';
    import MidArticle    from '.././components/landing_page/MidArticle.svelte';
    import CategoryBar   from '.././components/landing_page/CategoryBar.svelte';
    import Footer from '.././components/Footer.svelte';

    import isInViewport from '../assets/js/isInViewport.js';

    window.addEventListener("scroll", (e) => {
        let element = document.getElementById("goc-underline");
        if (isInViewport(element)) {
            element.classList.remove("w-0");
            element.classList.add("w-[75%]");
        }
    });

    let values = [
        {
            imgSrc: "", 
            gameName: "", 
            categoryPage: "", 
            articleTitle: "", 
            authorName: "", 
            articleDate: "", 
            authorPage: "", 
            articlePage: ""
        },
        {
            title: "",
            seeAllPage: "",
            contents: [
                {name: "", icon: "", image: ""},
                {name: "", icon: "", image: ""},
                {name: "", icon: "", image: ""},
                {name: "", icon: "", image: ""},
                {name: "", icon: "", image: ""},
                {name: "", icon: "", image: ""},
                {name: "", icon: "", image: ""},
                {name: "", icon: "", image: ""},
                {name: "", icon: "", image: ""}
            ]
        },
        [
            {
                title: "", 
                seeAllPage: "",
                contents: [
                    { 
                        gameName: "", 
                        title: "", 
                        authorPhotoSrc: "", 
                        authorName: "", 
                        postDate: "", 
                        articlePage: ""
                    },
                    { 
                        gameName: "", 
                        title: "", 
                        authorPhotoSrc: "", 
                        authorName: "", 
                        postDate: "", 
                        articlePage: ""
                    },
                    { 
                        gameName: "", 
                        title: "", 
                        authorPhotoSrc: "", 
                        authorName: "", 
                        postDate: "", 
                        articlePage: ""
                    },
                    { 
                        gameName: "", 
                        title: "", 
                        authorPhotoSrc: "", 
                        authorName: "", 
                        postDate: "", 
                        articlePage: ""
                    },
                ]
            }, 
            {
                title: "", 
                seeAllPage: "",
                contents: [
                    { 
                        gameName: "", 
                        title: "", 
                        authorPhotoSrc: "", 
                        authorName: "", 
                        postDate: "", 
                        articlePage: ""
                    },
                    { 
                        gameName: "", 
                        title: "", 
                        authorPhotoSrc: "", 
                        authorName: "", 
                        postDate: "", 
                        articlePage: ""
                    },
                    { 
                        gameName: "", 
                        title: "", 
                        authorPhotoSrc: "", 
                        authorName: "", 
                        postDate: "", 
                        articlePage: ""
                    },
                    { 
                        gameName: "", 
                        title: "", 
                        authorPhotoSrc: "", 
                        authorName: "", 
                        postDate: "", 
                        articlePage: ""
                    },
                ]
            }
        ],
        {
            contents: [
                ["", "", "", ""],
                ["", "", "", ""],
                ["", "", "", ""],
                ["", "", "", ""],
                ["", "", "", ""]
            ]
        }, 
        [
            { 
                gameTitle: "",
                description: "",
                categoryPage: "",
            },
            {
                gameTitle: "",
                description: "",
                categoryPage: "",
            },
            {
                gameTitle: "",
                description: "",
                categoryPage: "",
            }
        ]
    ]

    import { requestApi } from '../api/api_connection.js';

    async function getContent() {
        let payload = await requestApi("index/0");
        let response = await payload.json();

        if (response)
            values = response;
    }

    getContent();
</script>

<svelte:head>
    <title>{$title()}</title> 
</svelte:head>

<div class="w-full min-h-screen bg-color-0">
    <Header className="z-50 sticky top-0" />
    <MainArticle {...values[0]} />

    <div class="mt-12">
        <SimpleSection className="mt-8" elementType={BulletTipItem} {...values[1]} />

        <hr class="max-w-[1024px] mx-auto mt-14 mb-20">

        <div class="flex flex-col gap-20 mt-4">
            {#each values[2] as value}
                <SimpleSection elementType={PopUpArticle} {...value} />
            {/each}

            <MidArticle {...values[3]} />
        </div>
    </div>

    <div class="mt-40">
        <div class="w-fit mx-auto">
            <h2 class="text-color-title text-[38px] font-title-regular text-center">TIPS FOR YOUR GAME OF CHOICE</h2>
            <hr id="goc-underline" 
                class="w-0 mx-auto border-[1px] border-[#1E9B8F] dark:border-[#69D3C9] transition-all delay-300 duration-1000">
        </div>

        <div class="flex flex-col gap-[100px] mt-[100px]">
            {#each values[4] as value}
                <CategoryBar {...value} /> 
            {/each}
        </div>
    </div>

    <Footer className="mt-40"/>
</div>


<style>
  
</style>

